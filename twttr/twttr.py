def main():
    word=list(input("Input: "))
    string=shorten(word)
def shorten(word):
    li=["a","e","i","o","u","A","E","I","O","U"]
    j=0
    word=list(word)
    s=word
    while j<len(s):
        if string[j] in li:
            string.pop(j)
        else:
            j+=1
    return word
main()
