from brain import think
from tools import show_help


def main():
    print("Pocket AI Agent Started!")
    print("Type /help to see commands.")
    print("Type /quit to exit.")

    while True:
        try:
            text = input("> ").strip()

            if text == "/quit":
                print("Bye!")
                break

            if text == "/help":
                show_help()
                print("/remember key value: Store information")
                print("/recall key: Retrieve information")
                print("/memory: Show stored information")
                continue

            if not text:
                continue

            response = think(text)
            print(response)

        except KeyboardInterrupt:
            print("\nBye!")
            break


if __name__ == "__main__":
    main()