def main():
    y=div()
    z=y*100
    if 1<z<99:
        print(f"{z:.0f}%")
    elif z>100:
        main()
    elif z<=1:
        print("E")
    else:
        print("F")







def div():
    a=input("fraction: ")
    if isvalid(a):
        first,last=a.split("/")
    else:
        div()
    while True:
        try:
            x=int(first)/int(last)
            return x
        except (ValueError,ZeroDivisionError):
            div()
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
