from typing import Dict, Any, List
from functools import partial
from modules.MalType import MalType
from modules.Env import Env
from modules.read import read_str
from modules.MalError import MalError

def eval_ast(ast: MalType, env: Env) -> MalType:
    if not ast.isCollection():
        if ast.type == 'symbol':
            return env.get(ast)
            
    if ast.isCollection():
        if ast.type == 'list':
            contents = [eval(x, env) for x in ast.data]
            return contents
    return ast

def eval(ast: MalType, env: Env) -> MalType:
    def fn(env: Env, binds: MalType, body: MalType, exprs: MalType):
        newEnv = Env(env, binds.data, exprs)
        return eval(body, newEnv)

    # print(f"eval({ast})")
    while True:
        # print(f"ast = {ast}")
        if ast.isType('error'):
            return ast

        if not ast.isCollection():
            return eval_ast(ast, env)
        
        if ast.isEmpty():
            return ast
        if ast.type == "vector":
            return MalType.vector([eval(x, env) for x in ast.data])
        if ast.type == "hashmap":
            return MalType.hashmap([eval(x, env) for x in ast.data])

        first = ast.data[0].data
        
        if first == 'def!':
            env.set(ast.data[1].data, eval(ast.data[2], env))
            return env.get(ast.data[1])

        if first == 'env':
            print(env)
            return MalType.nil()

        if first == 'let*':
            args = ast.data[1]
            keys = args.data[::2]
            vals = args.data[1::2]
            newEnv = Env(env)
            for key, val in zip(keys, vals):
                newEnv.set(key.data, eval(val, newEnv))
            env = newEnv
            ast = ast.data[2]
            continue

        if first == 'do':
            ast = eval_ast(MalType.list(ast.data[1:]), env)[-1]
            continue

        if first == 'if':
            result = eval(ast.data[1], env)
            if result.type not in ['false', 'nil']:
                ast = ast.data[2]
                continue
            if len(ast.data) < 4:
                return MalType.nil()
            ast = ast.data[3]
            continue

        if first == 'swap!':
            target = ast.data[1]
            ast = eval_ast(ast, env)
            func = ast[2]
            data = [ast[1].data]
            if len(ast) > 3:
                data += ast[3:]
            if func.builtin == True:
                result = func.data(data)
            else:
                ast = func.ast
                newEnv = Env(func.env, func.params, data)
                result = eval(ast, newEnv)
            env.get(target).data = result
            return result

        if first == 'reset!':
            env.get(ast.data[1]).data = eval(ast.data[2], env)
            return env.get(ast.data[1]).data

        if first == 'fn*':
            result = MalType.function(partial(fn, env, ast.data[1], ast.data[2]))
            result.ast = ast.data[2]
            result.params = ast.data[1].data
            result.env = env
            return result

        ast = eval_ast(ast, env)
        func = ast[0]
        data = ast[1:]
        if func.builtin == True:
            return func.data(data)
        else:
            ast = func.ast
            env = Env(func.env, func.params, data)



        
    
