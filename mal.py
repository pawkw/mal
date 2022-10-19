from functions.read import read
from functions.eval import eval
from functions.print_mal import print_mal

def rep(exp: str) -> str:
    return print_mal(eval([read(exp)], []))

if __name__ == "__main__":
    while True:
        try:
            line = input('user> ')
            if not line:
                break
            rep(line)
        except EOFError:
            print("\nExiting.")
            break
        except Exception as e:
            print(f"\nError: {e.with_traceback()}")
            exit(1)