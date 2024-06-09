def main():
    time=input("What time is it? ")
    time=time.strip()
    y=convert(time)
    if 7.0<=y<=8.0:
        print("breakfast time")
    if 12.0<=y<=13.0:
        print("lunch time")
    if 18.0<=y<=19.0:
        print("dinner time")


def convert(time):
    x,y=time.split(":")
    z=float(x)+float(y)/60
    return z
if __name__ == "__main__":
    main()
