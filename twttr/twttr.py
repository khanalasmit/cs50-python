string=input()
string=list(string)
i=0
while i<len(string):
    if string[i]=="a" or string[i]=="e" or string[i]=="i" or string[i]=="o" or string[i]=="u":
        string.pop(i)
    i+=1
for x in string:
    print(x,end="")
