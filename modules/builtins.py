from functools import reduce
from modules.MalType import MalType
from modules.print_mal import pr_str
from typing import List

def mal_pr_str(args):
    result = []
    for x in args:
        result.append(pr_str(x, True))
    return MalType.string(" ".join(result))

def mal_prn(args):
    print(mal_pr_str(args).data)
    return MalType.nil()

def mal_str(args: List, sep: str):
    result = []
    for x in args:
        result.append(pr_str(x, False))
    return MalType.string(sep.join(result))

def mal_println(args):
    print(mal_str(args, "").data)
    return MalType.nil()

builtins = {
    '+': MalType.function(lambda args, _: reduce(lambda x, y: MalType.integer(x.data + y.data), args), builtin=True),
    '-': MalType.function(lambda args, _: reduce(lambda x, y: MalType.integer(x.data - y.data), args), builtin=True),
    '*': MalType.function(lambda args, _: reduce(lambda x, y: MalType.integer(x.data * y.data), args), builtin=True),
    '/': MalType.function(lambda args, _: reduce(lambda x, y: MalType.integer(x.data // y.data), args), builtin=True),
    '%': MalType.function(lambda args, _: reduce(lambda x, y: MalType.integer(x.data % y.data), args), builtin=True),
    'def!': MalType.symbol('def!'),
    'let*': MalType.symbol('let*'),
    'do': MalType.symbol('do'),
    'if': MalType.symbol('if'),
    'fn*': MalType.symbol('fn*'),
    'env': MalType.symbol('env'),
    'prn': MalType.function(lambda args, _: mal_prn(args)),
    'pr-str': MalType.function(lambda args, _: mal_pr_str(args)),
    'str': MalType.function(lambda args, _: mal_str(args, " ")),
    'println': MalType.function(lambda args, _: mal_println(args))
}