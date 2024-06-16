def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    li="1234567890"
    li2="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    li3="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s=list(s)
    if 2<=len(s)<=6:
        pass
    else:
        return False
    for char in s:
        if char not in li2:
            return False
    i=0
    while i<2:
        if s[i] not in li3:
            return False
        i+=1
    if s[len(s)-2]=="0":
        return False
    for i in range(2, len(s)):
        if s[i] in li:
            return False
        else:
            pass
    return True



main()
