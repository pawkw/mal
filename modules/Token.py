from dataclasses import dataclass

@dataclass
class Token:
    start: int
    end: int
    token_str: str

if __name__ == "__main__":
    mytoken = Token(start = 0, end = 1, token_str="(")
    print(mytoken)
