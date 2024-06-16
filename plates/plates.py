def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    li = "1234567890"
    li2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    li3 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Check the length of the plate
    if not (2 <= len(s) <= 6):
        return False

    # Check if all characters are alphanumeric
    for char in s:
        if char not in li2:
            return False

    # Check if the first two characters are letters
    if not (s[0] in li3 and s[1] in li3):
        return False

    # Check if the plate ends in "0"
    if s[len(s)-2]=="0":
        return False

    # Check if numbers appear in between letters
    found_number = False
    for i in range(2, len(s)):
        if s[i] in li:
            found_number = True
        elif found_number:
            return False

    # If all checks pass, the plate is valid
    return True


if __name__ == "__main__":
    main()
