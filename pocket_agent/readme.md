# Pocket AI Agent 🤖

A simple command-line AI agent built with Python as part of my 8 Weeks of AI Agents learning journey.

## Features

- Personalized greeting using command-line arguments (`--name`)
- Calculator (`/calc`)
- Current time (`/time`)
- Coin flip (`/flip`)
- Weather information (`/weather`)
- Simple conversational responses
- Memory commands (`/remember`, `/recall`, `/memory`)
- Help menu (`/help`)

## Project Structure

```text
pocket_agent/
├── main.py
├── brain.py
├── tools.py
├── memory.py
└── README.md
```

## Requirements

- Python
- UV package manager
- Required dependencies listed in `pyproject.toml`

## How to Run

```bash
uv run python main.py --name Abhinav
```

## Available Commands

| Command | Description |
|---|---|
| `/help` | Show available commands |
| `/calc 2 * 21` | Calculate an expression |
| `/time` | Show current time |
| `/flip` | Toss a coin |
| `/weather delhi` | Get weather |
| `/remember key value` | Store information |
| `/recall key` | Retrieve information |
| `/memory` | Show stored memory |
| `/quit` | Exit the agent |

## What I Learned

- Python modules and imports
- Functions and dictionaries
- Command-line arguments using argparse
- Basic agent architecture
- Tool execution and memory management
- Using UV to manage Python projects

---

Built as part of my **AI Agents – 8 Weeks** learning journey.