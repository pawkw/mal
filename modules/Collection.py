from typing import List

class Collection:
    TYPES = ("list", "vector", "hashmap")

    def __init__(self, type, contents: List, start: str, end: str) -> None:
        self.type = type
        self.contents = contents
        self.start = start
        self.end = end

    @classmethod
    def list(cls, contents) -> "Collection":
        return cls(cls.TYPES[0], contents, '(', ')')

    @classmethod
    def vector(cls, contents) -> "Collection":
        return cls(cls.TYPES[1], contents, '[', ']')

    @classmethod
    def hashmap(cls, contents) -> "Collection":
        items = iter(contents)
        items = iter(contents)
        result = dict(zip(items, items))
        return cls(cls.TYPES[2], result, '{', '}')