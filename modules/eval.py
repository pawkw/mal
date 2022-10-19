from typing import Dict, Any
from modules.Collection import Collection
from modules.Atom import Atom

def eval_ast(ast: Any, env: Dict) -> Collection:
    if isinstance(ast, Atom):
        if ast.type == 'symbol':
            if ast.string in env:
                return env[ast.string]
            else:
                raise Exception(f"{ast.string} not found in current namespace.")
    if isinstance(ast, Collection):
        if ast.type == 'list':
            contents = [eval(x, env) for x in ast.contents]
            return contents
    return ast

def eval(ast: Any, env: Dict) -> Collection:
    if isinstance(ast, Collection):
        if ast.type == "list":
            if len(ast.contents) == 0:
                return ast
            ast = eval_ast(ast, env)
            func = ast[0]
            result = func(*ast[1:])
            return result
        if ast.type == "vector":
            if len(ast.contents) == 0:
                return ast
            return Collection.vector([eval(x, env) for x in ast.contents])
        if ast.type == "hashmap":
            if len(ast.contents) == 0:
                return ast
            result = []
            for key, value in ast.contents.items():
                result.append(key)
                result.append(eval(value, env))
            return Collection.hashmap(result)
    else:
        return eval_ast(ast, env)
    return ast
