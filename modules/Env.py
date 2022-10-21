from modules.MalType import MalType
from typing import Any

class Env:
    def __init__(self, parent: "Env") -> None:
        self.data = {}
        self.parent = parent

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
            # print(f"Found {key}")
            return self

        if self.parent is None:
            # print("Parent is None.")
            return None

        return self.parent.find(key)

    def get(self, key):
        result = self.find(key)
        if result is None:
            return MalType.nil()
        return result.data[key]
