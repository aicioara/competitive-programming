BLACK = "\u001b[30m"
RED = "\u001b[31m"
GREEN = "\u001b[32m"
YELLOW = "\u001b[33m"
PURPLE = "\u001b[34m"
PINK = "\u001b[35m"
CYAN = "\u001b[36m"
WHITE = "\u001b[37m"
NC = CLEAR = "\u001b[0m"

def black(s):
    return f"{BLACK}{s}{NC}"

def red(s):
    return f"{RED}{s}{NC}"

def green(s):
    return f"{GREEN}{s}{NC}"

def yellow(s):
    return f"{YELLOW}{s}{NC}"

def purple(s):
    return f"{PURPLE}{s}{NC}"

def pink(s):
    return f"{PINK}{s}{NC}"

def cyan(s):
    return f"{CYAN}{s}{NC}"

def white(s):
    return f"{WHITE}{s}{NC}"
