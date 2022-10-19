from modules.Atom import Atom

builtins = {
    '+': lambda x, y: Atom.integer(x.value + y.value),
    '-': lambda x, y: Atom.integer(x.value - y.value),
    '*': lambda x, y: Atom.integer(x.value * y.value),
    '/': lambda x, y: Atom.integer(x.value//y.value),
    '%': lambda x, y: Atom.integer(x.value%y.value),
}