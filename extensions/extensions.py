ext=input("Extenstions: ")
ext=ext.strip()
x=int(ext.rfind("."))
string=ext[x+1:].lower()
match string:
    case "gif":
        print(f"image/{string}")
    case "jpg":
        print(f"image/{string}")
    case "jpeg":
        print(f"image/{string}")
    case "png":
        print(f"image/{string}")
    case "pdf":
        print(f"application/{string}")
    case "txt":
        print(f"image/{string}")
    case "zip":
        print(f"image/{string}")
    case _:
        print("application/octet-stream")
