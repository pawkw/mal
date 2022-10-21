from typing import Dict, Any
# from modules.Collection import Collection
# from modules.Atom import Atom
from modules.MalType import MalType

def eval_ast(ast: MalType, env: Dict) -> MalType:
    if not ast.isCollection():
        if ast.type == 'symbol':
            if ast.data in env:
                return env[ast.data]
            else:
                raise Exception(f"{ast.data} not found in current namespace.")
    if ast.isCollection():
        if ast.type == 'list':
            contents = [eval(x, env) for x in ast.data]
            return contents
    return ast

def eval(ast: MalType, env: Dict) -> MalType:
    if ast.isCollection():
        if ast.isEmpty():
            return ast
        if ast.type == "list":
            ast = eval_ast(ast, env)
            func = ast[0]
            result = func(*ast[1:])
            return result
        if ast.type == "vector":
            return MalType.vector([eval(x, env) for x in ast.data])
        if ast.type == "hashmap":
            return MalType.hashmap([eval(x, env) for x in ast.data])

    return eval_ast(ast, env)
