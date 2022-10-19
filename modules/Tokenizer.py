import re
from Token import Token
# Taken from Make a Lisp project.
pattern = re.compile(r"""[\s,]*(~@|[\[\]{}()'`~^@]|"(?:[\\].|[^\\"])*"?|;.*|[^\s\[\]{}()'"`@,;]+)""");

def tokenizer(string: str) -> str:
    for token in re.finditer(pattern, string):
        yield (Token(start = token.start(), end = token.end(), token_str = string[token.start():token.end()].strip()))

if __name__ == "__main__":
    tokens = tokenizer("(add 12 23)")
    for token in tokens:
        print(token)