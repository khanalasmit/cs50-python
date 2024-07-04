def main():
    greet=input("Greeting: ")
    val=int(value(greet))
    print(val)
def value(greeting):
    greeting=greeting.lower().strip()
    if greeting[0:5]=="hello":
        return 0
    elif greeting[0]=="h":
        return 20
    elif greeting[0]!="h":
        return 100



if __name__ == "__main__":
    main()
