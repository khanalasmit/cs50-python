import random

def main():
    level=get_level()
    j=0
    for i in range(10):
        num1=generate_integer(level)
        num2=generate_integer(level)
        sum=num1+num2
        count=0
        while count<3:
            try:
                ans=int(input(f"{num1} + {num2} = "))
                if ans!=sum:
                    count+=1
                    print("EEE")
                    if count==3:
                        print(f"{num1} + {num2} = {sum}")
                    continue
                elif ans==sum:
                    j+=1
                    break
            except (ValueError,TypeError):
                count+=1
                print("EEE")
                continue
    print(f"Score: {j}")


def get_level():
    try:
        lev=int(input("Level: "))
        while (lev>3) or (lev<=0):
            lev=int(input("Level: "))
        return lev
    except ValueError:
        get_level()


def generate_integer(level):
    if level==1:
        num=random.randrange(10)
        return num
    elif level==2:
        num=random.randrange(10,100)
        return num
    elif level==3:
        num=random.randrange(100,1000)
        return num



if __name__ == "__main__":
    main()
