from asyncore import read
from typing import List
from modules.Atom import Atom
from modules.Collection import Collection

def get_value(item: Atom, convert_strings) -> str:
    if item.type != "string" or not convert_strings:
        return item.string

    result = ""
    escape = False
    for char in item.value:
        if escape:
            if char == 'n':
                result += '\n'
            elif char == '\\':
                result += '\\'
            elif char == '"':
                result += '"'
            escape = False
                
        elif char == "\\":
            escape = True
            continue

        else:
            result += char
    return result


def mal_string(exp: Collection, readably) -> str:
    if not isinstance(exp, Collection):
        return (exp.type + ":" if readably else "") + get_value(exp, readably)
    result = exp.type + exp.start
    for item in exp.contents:
        if type(item) == Atom:
            result += " " + (item.type  + ":" if readably else "") + get_value(item, readably) + " "
        else:
            result += mal_string(item, readably)
    result += exp.end
    return result

def print_mal(exp: List, readably = True) -> None:
    print(mal_string(exp, True))