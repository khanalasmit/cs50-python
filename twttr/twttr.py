def main():
    string=list(input("Input: "))
    li=["a","e","i","o","u","A","E","I","O","U"]
    i=0
    string=list(string)
    while i<len(string):
        if string[i] in li:
            string.pop(i)
        i+=1
    for x in string:
        print(x,end="")
main()
