from typing import List
from modules.Reader import Reader
from modules.Token import Token
from modules.Atom import Atom

def read_atom(reader: Reader) -> Atom:
    string = reader.peek().token_str
    if string.isnumeric():
        result = Atom.integer(string, int(string))
    else:
        result = Atom.symbol(string, string)
    # reader.next()
    return result

def read_list(reader: Reader) -> List:
    result = []
    while True:
        token = reader.next()
        if not token:
            raise Exception(f"Expected ')' in {reader.string!r}")
        if token.token_str == ')':
            return result
        result.append(read_form(reader))

def read_form(reader: Reader) -> List:
    if reader.peek().token_str == '(':
        return read_list(reader)
    return read_atom(reader)

def read_str(string: str) -> str:
    reader = Reader(string)
    return read_form(reader)

if __name__ == "__main__":
    print(read_str("123"))
    print(read_str("(add (divide 123 456) 789)"))
