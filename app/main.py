import sys


def main():
    list = ["echo", "exit", "type"]
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
            print(" ".join(args[1:]))
        elif args[0] == "type":
            flag = False
            for x in list:
                if args[1] == x:
                    flag = True
                    break
            if flag:
                print(f"{args[1]} is a shell builtin")
            else:
                print(f"{args[1]} not found")
        else:
            print(f"{args[0]}: command not found")

if __name__ == "__main__":
    main()
