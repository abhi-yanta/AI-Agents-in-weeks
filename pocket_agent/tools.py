
import random
from datetime import datetime
from pathlib import Path
import sys

# Access existing Week 1 modules without moving them
sys.path.insert(0, str(Path(__file__).parent / "week1"))

from weather import weather_for


def calc(expr):
    """Calculate two numbers: /calc 2 * 21"""

    parts = expr.split()

    if len(parts) != 3:
        return "Usage: /calc 2 * 21"

    try:
        a = float(parts[0])
        b = float(parts[2])
    except ValueError:
        return "Numbers only!"

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


TOOLS = {
    "calc": calc,
    "time": now,
    "flip": flip,
    "weather": weather_for
}


def show_help():
    for name, fn in TOOLS.items():
        print(f"/{name}: {fn.__doc__}")
