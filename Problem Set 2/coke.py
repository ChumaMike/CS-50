

amount = 50
while amount > 0:
    coin = input("Insert Coin: ",)
    accepted = ["25", "10", "5"]
    if coin in accepted and amount > 0:
        amount -= int(coin)
        print(f"Amount due: {amount}", end="\n\n")
    else:
        print("Amount due: 50", end="\n\n")

if amount <= 0:
    print(f"Amount owed: {-1 * amount}")