greet=input("Greeting: ")
greet=greet.lower().strip()
if greet[0:5]=="hello":
    print("$0")
elif greet[0]=="h":
    print("$20")
elif greet[0]!="h":
    print("$100")
