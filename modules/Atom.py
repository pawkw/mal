from typing import Any, List

class Atom:
    TYPES = ("integer", "symbol", "string", "nil", "true", "false", "hashkey", "comment")

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
    def symbol(cls, string: str) -> "Atom":
        return cls(string, cls.TYPES[1], string)
    
    @classmethod
    def string(cls, string: str, value: str) -> "Atom":
        return cls(string, cls.TYPES[2], value)

    @classmethod
    def nil(cls) -> "Atom":
        return cls("nil", cls.TYPES[3], "nil")

    @classmethod
    def true(cls) -> "Atom":
        return cls("true", cls.TYPES[4], "true")

    @classmethod
    def false(cls) -> "Atom":
        return cls("false", cls.TYPES[5], "false")

    @classmethod
    def hashkey(cls, string: str) -> "Atom":
        return cls(":"+string, cls.TYPES[6], string)

    @classmethod
    def comment(cls, string: str) -> "Atom":
        return cls(string, cls.TYPES[7], string)