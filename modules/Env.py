from modules.MalType import MalType
from typing import Any
from modules.MalError import MalError

class Env:
    def __init__(self, parent: "Env", binds = None, exprs = None) -> None:
        self.data = {}
        self.parent = parent
        
        if binds:
            for index in range(len(binds)):
                if binds[index].data == "&":
                    self.set(binds[index+1].data, MalType.list(exprs[index:]))
                    break
                self.set(binds[index].data, exprs[index])
 
    def __str__(self) -> str:
        result = ""
        for pair in self.data.items():
            result += "" if pair[1].isType('function') and pair[1].builtin else f"{pair[0]} -> {pair[1]}\n"
        if self.parent is not None:
            result += "PARENT ENV:\n"
            result += self.parent.__str__()
        return result

    def set(self, key: MalType, value: Any) -> None:
        self.data[key] = value

    def find(self, key: MalType) -> "Env":
        if key in self.data:
            return self

        if self.parent is None:
            return None

        return self.parent.find(key)

    def get(self, key: MalType):
        result = self.find(key.data)
        if result is None:
            raise MalError(f"{key} not found.")
        return result.data[key.data]

    def getRoot(self) -> "Env":
        if self.parent is None:
            return self
        return self.getRoot()
