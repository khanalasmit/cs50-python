def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    i=0
    li=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    li2=["1","2","3","4","5","6","7","8","9","0"]
    if 2<=len(s)<=6:
        while i<2:
            if s[i] in li:
                j=1
                while j<(len(s)-1):
                    if s[j] not in li2:
                        k=0
                        while k<len(s):
                            if s[k] in li or s[k] in li2:
                                return True
                            k+=1
                    j+=1
            i+=1


main()
