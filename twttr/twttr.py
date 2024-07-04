def main():
    string=list(input("Input: "))
    
def shorten(word):
    li=["a","e","i","o","u","A","E","I","O","U"]
    j=0
    string=list(string)
    s=string
    while j<len(s):
        if string[j] in li:
            string.pop(j)
        else:
            j+=1
    for x in string:
        print(x,end="")
main()
