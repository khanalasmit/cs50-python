import sys

def main():
    if len(sys.argv) > 2:
        if ".py" in sys.argv[2]:
            return
    if len(sys.argv)<2:
        print("Too few command-line arguments")
        return
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
