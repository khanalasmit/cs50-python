amount=None
sum=0
while True:
    amount=int(input("Insert coin: "))
    if amount==25 or amount==10 or amount==5:
        sum+=amount
    if sum<50:
        print(f"Amount due: {50-sum}")
    elif sum>=50:
        print(f"Change owned: {sum-50}")
        break

