greeting = input("Greet: ").lower().strip()

if greeting.startswith("hello"):
    print("$0")

elif greeting.startswith("h") and greeting != "hello":
    print("$20")
    
else:
    print("$100")

