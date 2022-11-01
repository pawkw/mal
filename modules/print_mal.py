from typing import List, Any
# from modules.Atom import Atom
# from modules.Collection import Collection
from modules.MalType import MalType, delimiters

def get_value(item: MalType, convert_strings) -> str:
    if item.type == "function":
        return "#<function>"

    if item.type == "hashkey":
        return ':' + item.data[1:]

    if item.type != "string" or not convert_strings:
        return str(item.data)

    result = ""
    escape = False
    for char in item.data:
        if escape:
            if char == 'n':
                result += '\\n'
            elif char == '\\':
                result += '\\\\'
            elif char == '"':
                result += '\\"'
            escape = False
            continue
                
        if char == "\\":
            escape = True
            continue

        result += char
    return f'"{result}"'

def pr_str(item: MalType, print_readably: bool) -> str:
    if not item.isCollection():
        return get_value(item, print_readably)
    
    result = ""
    for exp in item.data:
        if not exp.isCollection():
            result += " " + get_value(exp, print_readably)
            continue
        result += " " + pr_str(exp, print_readably)
    result = delimiters[item.type]['start'] + result.strip() + delimiters[item.type]['end']
    return result

def print_mal(exp: MalType, readably = True) -> None:
    print(pr_str(exp, readably))
