from typing import List
from modules.Atom import Atom

def mal_string(exp: List) -> str:
    result = "("
    for item in exp:
        if type(item) == Atom:
            result += " " + item.string + " "
        else:
            result += mal_string(item)
    result += ")"
    return result

def print_mal(exp: List) -> None:
    print(mal_string(exp))