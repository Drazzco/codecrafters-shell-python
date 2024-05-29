import sys


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        # Wait for user input
        args = input().split()
        if args[0] == "exit":
            if args[1] == "0":
                sys.exit(0)
            else:
                command = args[0] + " " + args[1]
                print(f"{command}: command not found")
        elif args[0] == "echo":
            command = ""
            cont = 0
            for x in args:
                if cont > 0:
                    command += x + " "
                else:
                    cont = 1
            print(f"{command}")
        else:
            print(f"{args[0]}: command not found")

if __name__ == "__main__":
    main()
