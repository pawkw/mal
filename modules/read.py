from typing import List
from modules.Reader import Reader
# from modules.Atom import Atom
# from modules.Collection import Collection
from modules.MalType import MalType

def read_atom(reader: Reader) -> MalType:
    string = reader.peek().token_str
    if string.isnumeric():
        return MalType.integer(int(string))
    
    if string[0] == '"':
        if string[-1] == '"':
            return MalType.string(string[1:-1])
        raise Exception(f'Expected a " to close string {string}')

    if string[0] == ':':
        return MalType.hashkey(str(chr(255)) + string[1:])

    if string == 'true':
        return MalType.true()

    if string == 'nil':
        return MalType.nil()

    if string == 'false':
        return MalType.false()

    if string[0] == ';':
        return MalType.comment(string)

    return MalType.symbol(string)

def read_list(reader: Reader, delimiter: str) -> List:
    result = []
    while True:
        token = reader.next()
        if not token:
            raise Exception(f"Expected {delimiter} in {reader.string!r}")
        if token.token_str == delimiter:
            return result
        result.append(read_form(reader))

def read_form(reader: Reader) -> MalType:
    peek = reader.peek().token_str
    if peek == '(':
        return MalType.list(read_list(reader, ')'))
    if peek == '[':
        return MalType.vector(read_list(reader, ']'))
    if peek == '{':
        return MalType.hashmap(read_list(reader, '}'))
    return read_atom(reader)

def read_str(string: str) -> str:
    reader = Reader(string)
    return read_form(reader)

if __name__ == "__main__":
    print(read_str("123"))
    print(read_str("(add (divide 123 456) 789)"))
