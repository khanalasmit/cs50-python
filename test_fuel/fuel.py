def gauge(percentage):
    z=percentage*100
    return z

def main():
    a=input("fraction: ")
    y=convert(a)
    z=gauge(y)
    if 1<z<99:
        print(f"{z:.0f}%")
    elif z>100:
        main()
    elif z<=1:
        print("E")
    else:
        print("F")




def convert(fraction):
    if isvalid(fraction):
        first,last=fraction.split("/")
    else:
        convert()
    while True:
        try:
            x=int(first)/int(last)
            return x
        except (ValueError,ZeroDivisionError):
            convert()
            pass


def isvalid(a):
    li="1234567890abcdefghijklmnopqrstuvwxyz"
    for char in a:
        if char not in li:
            if char=="/":
                return True
            else:
                return False




if __name__=="__main__":
    main()
