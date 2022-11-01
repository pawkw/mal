from typing import Any, List

delimiters = {
    "hashmap": {"start": "{", "end": "}"},
    "vector": {"start": "[", "end": "]"},
    "list": {"start": "(", "end": ")"}}

class MalType:
    def __init__(self, type: str, data) -> None:
        self.type = type
        self.data = data
    
    def __repr__(self) -> str:
        if not self.isCollection():
            if self.type == "hashkey":
                return f"{self.type}: :{str(self.data[1:])}"
            if self.type in ["false", "true", "nil"]:
                return self.type
            return f"{self.type}: {str(self.data)}"

        if self.isEmpty():
            return f"{self.type}(empty)" 

        result = f"{self.type}{delimiters[self.type]['start']} "
        for item in self.data:
            result += f"{item} "
        result += f"{delimiters[self.type]['end']}"
        return result
        
    def isEmpty(self) -> bool:
        if self.isCollection() or self.type == "string":
            return len(self.data) < 1
        raise ValueError(f"{self.type} can not be empty.")

    def isType(self, query: str) -> str:
        return self.type == query

    def isCollection(self) -> bool:
        return self.type in ["hashmap", "vector", "list"]

    @classmethod
    def list(cls, contents: List) -> "MalType":
        return cls("list", contents)

    @classmethod
    def vector(cls, contents: List) -> "MalType":
        return cls("vector", contents)

    @classmethod
    def hashmap(cls, contents: List) -> "MalType":
        return cls("hashmap", contents)

    # Atoms
    @classmethod
    def integer(cls, contents: int) -> "MalType":
        return cls("integer", contents)

    @classmethod
    def symbol(cls, contents: str) -> "MalType":
        return cls("symbol", contents)

    @classmethod
    def string(cls, contents: str) -> "MalType":
        return cls("string", contents)

    @classmethod
    def nil(cls) -> "MalType":
        return cls("nil", 'nil')

    @classmethod
    def true(cls) -> "MalType":
        return cls("true", 'true')

    @classmethod
    def false(cls) -> "MalType":
        return cls("false", 'false')

    @classmethod
    def hashkey(cls, contents: str) -> "MalType":
        return cls("hashkey", contents)

    @classmethod
    def comment(cls, contents: str) -> "MalType":
        return cls("comment", contents)

    @classmethod
    def function(cls, contents: Any, builtin = False) -> "MalType":
        result = cls("function", contents)
        result.builtin = builtin
        return result
