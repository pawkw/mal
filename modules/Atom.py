from typing import Any

class Atom:
    TYPES = ("integer", "symbol")

    def __init__(self, string: str, type: str, value: Any) -> None:
        self.string = string
        self.type = type
        self.value = value

    def __repr__(self) -> str:
        return f"Atom({self.string!r} {self.type} {self.value})"

    @classmethod
    def integer(cls, string: str, value: int) -> "Atom":
        return cls(string, cls.TYPES[0], value)

    @classmethod
    def symbol(cls, string: str, value: str) -> "Atom":
        return cls(string, cls.TYPES[1], value)
