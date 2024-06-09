string=input("Expression: ")
x,y,z=string.split(" ")
if y=="+":
    a=float(x)+float(z)
elif y=="-":
    a=float(x)-float(z)
elif y=="*":
    a=float(x)*float(z)
elif y=="/":
    a=float(x)/float(z)
print(f"{a:.1f}")
