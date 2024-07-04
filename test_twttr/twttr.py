def main():
    word=input("Input: ")
    string=shorten(word)
    for x in string:
        print(x,end="")
    print()
def shorten(word):
    li=["A","E","I","O","U"]
    j=0
    word=list(word)
    s=word
    while j<len(s):
        if word[j] in li:
            word.pop(j)
        else:
            j+=1
    return str(word)
if __name__=="__main__":
    main()
