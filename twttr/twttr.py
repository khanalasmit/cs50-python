string=input("Input")
string=list(string)
i=0
s=string.lower()
while i<len(string):
    if s=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u":
        string.pop(i)
    i+=1
for x in string:
    print(x,end="")

