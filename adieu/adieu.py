import inflect
string=list("a")
string.remove("a")
def main():
    while True:
        try:
            name=input("Name: ")
            string.append(name)
        except EOFError:
            join(string)
            break
def join(string):
    p=inflect.engine()
    print(f"Adieu, adieu, to {p.join(string)}")
main()
