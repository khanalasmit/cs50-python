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
        sys.exit("Missing command-line argument")
    except ValueError:
        sys.exit("Command-line argument is not a number")
except requests.RequestException:
    sys.exit("Missing command-line argument")

