camel=list(input("camelCase: "))
i=0
letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("snake_case:",end="")
while i<len(camel):
    if camel[i] not in letters:
        print(camel[i],end="")
        i+=1
    elif camel[i] in letters:
        print("_",end="")
        camel[i]=camel[i].lower()
