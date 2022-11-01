from functools import reduce
from typing import List, Callable
from modules.MalType import MalType

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
    'fn*': MalType.symbol('fn*')
}