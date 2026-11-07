from tools import TOOLS
from memory import Memory
from pathlib import Path
import sys

# Access existing mood_bot.py
sys.path.insert(0, str(Path(__file__).parent / "week1"))

from mood_bot import reply


memory = Memory()


def think(text):
    """Process user input and decide what action to take."""

    text = text.strip()

    # Memory commands
    if text.startswith("/remember "):
        content = text[len("/remember "):]
        key, separator, value = content.partition(" ")

        if not separator:
            return "Usage: /remember name Abhinav"

        memory.remember(key, value)
        return f"I'll remember {key}: {value}"

    if text.startswith("/recall "):
        key = text[len("/recall "):].strip()
        return memory.recall(key)

    if text == "/memory":
        return memory.show_all()

    # Tool commands
    if text.startswith("/"):
        name, _, args = text[1:].partition(" ")

        if name in TOOLS:
            if name in ("calc", "weather"):
                return TOOLS[name](args)

            return TOOLS[name]()

    # Normal conversation
    return reply(text)