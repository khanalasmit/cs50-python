greet=input("Greeting: ")
greet=greet.lower().strip()
if greet[0:6]=="hello":
    print("$0")
elif greet[0]=="h":
    print("$20")
elif greet[0]!="h":
    print("$100")
