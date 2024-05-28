import sys


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        # Wait for user input
        if command := input().strip():
            if command == "exit 0":
                sys.exit(0)
            else:
                print(f"{command}: command not found")


if __name__ == "__main__":
    main()
