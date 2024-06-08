def main():
    string=input()
    convert(string)
def convert(new_string):
    print(new_string.replace(":)","\N{slightly smiling face}").replace(":(","\N{slightly frowning face}"))
main()
