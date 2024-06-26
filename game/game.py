import random
n=int(input("Level: "))
def guess():
    guess=input("Guess: ")
    return guess
while True:
    num=random.randrange(1,n)
    try:
        number=int(guess())
        if number<=0:
            continue
        elif number==num:
            print("Just right")
            exit()
        elif number<num:
            print("Too small!")
            continue
        elif number>num:
            print("Too large!")
            continue
    except TypeError:
        pass
