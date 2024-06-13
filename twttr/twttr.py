string=input("Input")
string=list(string)
i=0
while i<len(string):
    if string.lower()[i]=="a" or string.lower()[i]=="e" or string.lower()[i]=="i" or string.lower()[i]=="o" or string.lower()[i]=="u":
        string.pop(i)
    i+=1
for x in string:
    print(x,end="")

