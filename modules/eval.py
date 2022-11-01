from typing import Dict, Any, List
# from modules.Collection import Collection
# from modules.Atom import Atom
from modules.MalType import MalType
from modules.Env import Env

def apply(ast: MalType, env: Env) -> MalType:
    first = ast.data[0]
    if first.data == 'def!':
        env.set(ast.data[1].data, eval(ast.data[2], env))
        return env.get(ast.data[1].data)

    if first.data == 'let*':
        newEnv = Env(env)
        args = ast.data[1]
        keys = args.data[::2]
        vals = args.data[1::2]
        while keys:
            newEnv.set(keys.pop().data, eval(vals.pop(), env))
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

    ast = eval_ast(ast, env)
    result = ast[0].data(ast[1:])
    return result

def eval_ast(ast: MalType, env: Env) -> MalType:
    if not ast.isCollection():
        if ast.type == 'symbol':
            result = env.get(ast.data)
            if result.type != 'nil':
                return result
            raise Exception(f"{ast.data} not found in scope.\n{env}")
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

    return eval_ast(ast, env)
