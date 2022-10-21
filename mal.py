import builtins
import traceback
from modules.read import read_str
from modules.eval import eval
from modules.print_mal import print_mal
from modules.builtins import builtins
from modules.Env import Env

root_env = Env(None)
for func in builtins.items():
    root_env.set(func[0], func[1])

def rep(exp: str) -> str:
    return print_mal(eval(read_str(exp), root_env))

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
        