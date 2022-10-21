from numpy import integer
from modules.MalType import MalType

builtins = {
    '+': lambda x, y: MalType.integer(x.data + y.data),
    '-': lambda x, y: MalType.integer(x.data - y.data),
    '*': lambda x, y: MalType.integer(x.data * y.data),
    '/': lambda x, y: MalType.integer(x.data//y.data),
    '%': lambda x, y: MalType.integer(x.data%y.data),
}