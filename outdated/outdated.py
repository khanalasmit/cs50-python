months=dict(
    January="1",
    February="2",
    March="3",
    April="4",
    May="5",
    June="6",
    July="7",
    August="8",
    September="9",
    October="10",
    November="11",
    December="12"
)
def main():
    date=input("Date: ")
    li="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if date[0].upper() in li:
        if validate(date):
            first,second,third=date.split(" ")
            second=second.replace(","," ").strip()
            if len(second)==1 and len(months[first])==1:
                print(f"{third}-0{months[first]}-0{second}")
            elif len(second)==1:
                print(f"{third}-{months[first]}-0{second}")
            elif len(months[first])==1:
                print(f"{third}-0{months[first]}-{second}")

        else:
            pass
    elif date[0] not in li:
        if isvalid(date):
            fi,sec,thi=date.split("/")
            fi=fi.strip()
            sec=sec.strip()
            thi=thi.strip()
            if len(sec)==1 and len(fi)==1:
                print(f"{thi}-0{fi}-0{sec}")
            elif len(sec)==1 and len(fi)==2:
                print(f"{thi}-{fi}-0{sec}")
            elif len(fi)==1 and len(sec)==2:
                print(f"{thi}-0{fi}-{sec}")
            else:
                print(f"{thi}-{fi}-{sec}")
        else:
            pass
def validate(date):
    if "," in date:
        first,sec,third=date.split(" ")
        if first in months:
            return True
        else:
            main()
    else:
        main()
def isvalid(date):
    if "/" in date:
        first,second,third=date.split("/")
        if int(first)<=12 and int(second)<=30:
            return True
        else:
            main()
    else:
        main()
main()
