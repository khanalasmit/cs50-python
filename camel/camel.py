def main():
    camelcase=input("camelCase: ")
    index=snake(camelcase)
    camelcase=list(camelcase)
    i=0
    print("snake_case:",end="")
    while i<index:
        print(camelcase[i],end="")
        i+=1
    print("_",end="")
    camelcase[index]=camelcase[index].lower()
    while index<len(camelcase):
        print(camelcase[index],end="")
        index+=1
def snake(camelcase):
    camelcase=list(camelcase)
    letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    i=0
    while i<len(camelcase):
        if camelcase[i] in letters:
            return i
        i+=1
main()
