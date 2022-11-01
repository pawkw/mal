from functools import reduce
import operator
from modules.MalType import MalType
from modules.print_mal import pr_str
from typing import List

def mal_pr_str(args):
    result = []
    for x in args:
        result.append(pr_str(x, False))
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

def mal_compare(args, op):
    result = MalType.true() if op(args[0].data, args[1].data) else MalType.false()
    if len(args) < 3:
        return result
    return MalType.true() if result.isType('true') and mal_compare(args[1:], op).isType('true') else MalType.false()

def mal_equate(args):
    if len(args) < 3:
        if args[0].type == args[1].type or args[0].isCollection() and args[1].isCollection():
            if not args[0].type in ['list', 'vector']:
                return MalType.true() if args[0].data == args[1].data else MalType.false()
            if len(args[0].data) != len(args[1].data):
                return MalType.false()
            for x, y in zip(args[0].data, args[1].data):
                if mal_equate([x, y]).isType('false'):
                    return MalType.false()
            return MalType.true()
        return MalType.false()
    rest = mal_equate(args[1:])
    result = mal_equate([args[0], args[1]])
    return MalType.true() if rest.isType('true') and result.isType('true') else MalType.false()

builtins = {
    '+': MalType.function(lambda args: reduce(lambda x, y: MalType.integer(x.data + y.data), args), builtin=True),
    '-': MalType.function(lambda args: reduce(lambda x, y: MalType.integer(x.data - y.data), args), builtin=True),
    '*': MalType.function(lambda args: reduce(lambda x, y: MalType.integer(x.data * y.data), args), builtin=True),
    '/': MalType.function(lambda args: reduce(lambda x, y: MalType.integer(x.data // y.data), args), builtin=True),
    '%': MalType.function(lambda args: reduce(lambda x, y: MalType.integer(x.data % y.data), args), builtin=True),
    'def!': MalType.symbol('def!'),
    'let*': MalType.symbol('let*'),
    'do': MalType.symbol('do'),
    'if': MalType.symbol('if'),
    'fn*': MalType.symbol('fn*'),
    'env': MalType.symbol('env'),
    'prn': MalType.function(lambda args: mal_prn(args), builtin=True),
    'pr-str': MalType.function(lambda args: mal_pr_str(args), builtin=True),
    'str': MalType.function(lambda args: mal_str(args, " "), builtin=True),
    'println': MalType.function(lambda args: mal_println(args), builtin=True),
    'list': MalType.function(lambda args: MalType.list(args), builtin=True),
    'list?': MalType.function(lambda args: MalType.true() if args[0].isType('list') else MalType.false(), builtin=True),
    'empty?': MalType.function(lambda args: MalType.true() if len(args[0].data) < 1 else MalType.false(), builtin=True),
    'count': MalType.function(lambda args: MalType.integer(len(args[0].data)) if args[0].type in ['list', 'vector', 'hashmap'] else MalType.integer(0), builtin=True),
    '<': MalType.function(lambda args: mal_compare(args, operator.lt), builtin=True),
    '<=': MalType.function(lambda args: mal_compare(args, operator.le), builtin=True),
    '>': MalType.function(lambda args: mal_compare(args, operator.gt), builtin=True),
    '>=': MalType.function(lambda args: mal_compare(args, operator.ge), builtin=True),
    '=': MalType.function(lambda args: mal_equate(args), builtin=True)
}