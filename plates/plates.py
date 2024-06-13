def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if 2<=len(s)<=6:
        if s[:len(s)].isalpha():
            if s[:2].isalpha():
                if s[-1:].isalpha():
                    return True

main()
