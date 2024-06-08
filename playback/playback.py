def main():
    string=input()
    next_string=convert(string)
    print(next_string)

def convert(new_string):
    return (new_string.replace(":)","\N{slightly smiling face}").replace(":(","\N{slightly frowning face}"))
main()
