def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    i=0
    li2=["1","2","3","4","5","6","7","8","9","0"]
    li=["1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    while i<len(s):
        if s[i] in li:
            if s[1:len(s)] not in li2:
                if 2<=len(s)<=6:
                    return True
        i+=1

main()
