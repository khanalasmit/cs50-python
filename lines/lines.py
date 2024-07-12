import sys

def main():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    if "." not in sys.argv[1]:
        sys.exit("Not a python file")
    first,second=sys.argv[1].split(".")
    if second!="py":
        print("Not a Python file")
    i = 0
    try:
        with open(sys.argv[1], "r") as file:
            while True:
                line = file.readline()
                if not line:
                    break
                if line.strip() and not line.lstrip().startswith('#'):
                    i += 1
            print(i)
    except FileNotFoundError:
        print("File does not exists")

if __name__ == "__main__":
    main()
