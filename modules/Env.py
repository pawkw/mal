from modules.MalType import MalType
from typing import Any

class Env:
    def __init__(self, parent: "Env", binds = None, exprs = None) -> None:
        self.data = {}
        self.parent = parent
        if binds:
            for var, value in zip(binds, exprs):
                self.set(var.data, value)

    def __str__(self) -> str:
        result = ""
        for pair in self.data.items():
            result += f"{pair[0]} -> {pair[1]}\n"
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
            print("Parent is None.")
            return None

        return self.parent.find(key)

    def get(self, key: MalType):
        result = self.find(key.data)
        if result is None:
            return MalType.nil()
        return result.data[key.data]
