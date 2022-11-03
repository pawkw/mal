import builtins
from modules.MalType import MalType
from modules.read import read_str
from modules.eval import eval
from modules.print_mal import print_mal
from modules.builtins import builtins
from modules.Env import Env
from modules.MalError import MalError
import sys, traceback, atexit, readline

root_env = Env(None)
for func in builtins.items():
    root_env.set(func[0], func[1])

def rep(exp: str) -> str:
    return print_mal(eval(read_str(exp), root_env))

if __name__ == "__main__":
    atexit.register(readline.write_history_file, "./.malhistory")
    readline.read_history_file("./.malhistory")
    readline.set_history_length(100)
    
    eval(read_str('(def! load-file (fn* (f) (eval (read-string (str "(do " (slurp f) "\nnil)")))))'), root_env)
    eval(read_str('(def! not (fn* (a) (if a false true)))'), root_env)
    root_env.set('eval', MalType.function(lambda ast: eval(ast[0], root_env), builtin=True))

    root_env.set('*ARGV*', MalType.list([]))
    if len(sys.argv) > 1:
        root_env.set('*ARGV*', MalType.list([MalType.string(x) for x in sys.argv[1:]]))
        rep(f'(load-file "{sys.argv[1]}")')

    while True:
        try:
            line = input('user> ')
            if not line:
                break
            rep(line)
        except EOFError:
            print("\nExiting.")
            break
        except MalError as error:
            print(error.args[0])
        except Exception as error:
            print("".join(traceback.format_exception(*sys.exc_info())))
        