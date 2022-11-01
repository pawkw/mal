from typing import Dict, Any, List
from functools import partial
from modules.MalType import MalType
from modules.Env import Env

def apply(ast: MalType, env: Env) -> MalType:
    def fn(binds: MalType, body: MalType, exprs: MalType, env: Env):
        newEnv = Env(env, binds.data, exprs)
        return eval(body, newEnv)

    first = ast.data[0]
    
    if first.data == 'def!':
        env.set(ast.data[1].data, eval(ast.data[2], env))
        return env.get(ast.data[1])

    if first.data == 'env':
        print(env)
        return MalType.nil()

    if first.data == 'let*':
        args = ast.data[1]
        keys = args.data[::2]
        vals = args.data[1::2]
        newEnv = Env(env)
        for key, val in zip(keys, vals):
            newEnv.set(key.data, eval(val, newEnv))
        return eval(ast.data[2], newEnv)

    if first.data == 'do':
        return eval_ast(MalType.list(ast.data[1:]), env)[-1]

    if first.data == 'if':
        result = eval(ast.data[1], env)
        if result.type not in ['false', 'nil']:
            return eval(ast.data[2], env)
        if len(ast.data) < 4:
            return MalType.nil()
        return eval(ast.data[3], env)

    if first.data == 'fn*':
        return MalType.function(partial(fn, ast.data[1], ast.data[2]))

    ast = eval_ast(ast, env)
    if ast[0].isType('error'):
        return ast[0]

    result = ast[0].data(ast[1:], env)
    return result

def eval_ast(ast: MalType, env: Env) -> MalType:
    if not ast.isCollection():
        if ast.type == 'symbol':
            result = env.get(ast)
            if not result.isType('nil'):
                return result
            return MalType.error(f"'{ast.data}' not found.")
    if ast.isCollection():
        if ast.type == 'list':
            contents = [eval(x, env) for x in ast.data]
            return contents
    return ast

def eval(ast: MalType, env: Env) -> MalType:
    if ast.isCollection():
        if ast.isEmpty():
            return ast
        if ast.type == "list":
            return apply(ast, env)
        if ast.type == "vector":
            return MalType.vector([eval(x, env) for x in ast.data])
        if ast.type == "hashmap":
            return MalType.hashmap([eval(x, env) for x in ast.data])

    if ast.isType('error'):
        return ast

    return eval_ast(ast, env)
