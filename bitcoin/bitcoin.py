import requests
import sys
try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    p = r.json()
    a=p["bpi"]["USD"]["rate_float"]
    try:
        b=float(sys.argv[1])
        amount=a*b
        print(f"{amount:,.4f}")
    except IndexError:
        print("Missing command-line argument")
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit()
except requests.RequestException:
    print("Missing command-line argument")
    sys.exit()

