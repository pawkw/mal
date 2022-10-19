from Token import Token
from Tokenizer import tokenizer

class Reader:
    def __init__(self, string: str) -> None:
        self.string = string
        self.tokenizer = tokenizer(string)
        self.current_token = next(self.tokenizer)

    def next(self) -> Token:
        try:
            self.current_token = next(self.tokenizer)
        except StopIteration:
            self.current_token = None
        return self.current_token

    def peek(self) -> Token:
        return self.current_token

if __name__ == "__main__":
    reader = Reader("(mul 12 23)")
    print(reader.peek())
    print(reader.peek())
    print(reader.next())

