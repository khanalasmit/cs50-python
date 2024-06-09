string=input("WHat is the Answer to the Great Question to Life, the Universe and Everything ? ")
new=string.lower().replace("-"," ")
if new.strip()=="42" or new.strip()=="forty two":
    print("YES")
else:
    print("NO")

