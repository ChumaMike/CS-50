import json
import sys
import requests



try:
    r = requests.get("https://api.coincap.io/v2/assets/bitcoin")
    nas = r.json()
    price = nas["data"]["priceUsd"]
    n = sys.argv[1]
    if n.isdigit() or (n.split(".")[0].isdigit() and n.split(".")[1].isdigit()):
        n = float(n)
        price = float(price)
        ans = price * n
        num = round(ans, 4)
        fn = f"{num:,.4f}"
        print(fn)

    else:
        sys.exit("Command-line argument is not a number")
        
except requests.RequestException:
    ...
except IndexError:
    sys.exit(("Missing commnandline agrument"))
