# while True:
#     word = input("Word> ").strip()
#     if word == "/quit":
#         print("Bye!")
#         break
#     else:
#         print("Hello,", word)
        
        
import random
from datetime import datetime
from mood_bot import reply


def calc(expr):
    """Calculate two numbers, e.g. /calc 2 * 21 (supports + - * /)."""
    parts = expr.split()
    if len(parts) != 3:
        return "Usage: /calc 2 * 21"
    try:
        a = float(parts[0])
        b = float(parts[2])
    except ValueError:
        return "Numbers only, e.g. /calc 2 * 21"
    op = parts[1]
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    return "Use + - * or /"


def now():
    """Show the current time."""
    return datetime.now().strftime("%H:%M:%S")


def flip():
    """Toss a coin."""
    return random.choice(["Heads", "Tails"])


TOOLS = {"calc": calc, "time": now, "flip": flip}


def show_help():
    for name, fn in TOOLS.items():
        print(f"/{name}: {fn.__doc__}")


while True:
    text = input("> ").strip()
    if text == "/quit":
        print("Bye!")
        break
    if text == "/help":
        show_help()
        continue
    if text.startswith("/"):
        name, _, args = text[1:].partition(" ")
        if name in TOOLS:
            if name == "calc":
                print(TOOLS[name](args))
            else:
                print(TOOLS[name]())
        else:
            print(reply(text))
    else:
        print(reply(text))