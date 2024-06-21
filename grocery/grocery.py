grocery=list("a")
i=0
while True:
    try:
        name=input().lower()
        i+=1
        grocery.append(name)
    except EOFError:
        break
grocery.remove("a")
grocery.sort()
j=0
count=1
li1=list("1")
li1.remove("1")
li2=list("a")
li2.remove("a")
for char in grocery:
    while j<len(grocery):
        if char==grocery[j]:
            count+=1
            grocery.remove(grocery[j])
        j+=1
    j=0
    li1.append(count)
    li2.append(char)
    count=0
for itm in li2:
    for cot in li1:
        print(cot,itm.upper())
        li1.remove(cot)
        break
