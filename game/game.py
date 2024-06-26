import random
while True:
    try:
        n=int(input("Level: "))
        if n<0:
            continue
        else:
            break
    except ValueError:
        pass
def guess():
    while True:
        try:
            guess=int(input("Guess: "))
            return guess
        except ValueError:
            pass
while True:
    num=random.randrange(1,n)
    try:
        number=int(guess())
        if number<=0:
            continue
        elif number==num:
            print("Just right!")
            exit()
        elif number<num:
            print("Too small!")
            continue
        elif number>num:
            print("Too large!")
            continue
    except ValueError:
        pass
