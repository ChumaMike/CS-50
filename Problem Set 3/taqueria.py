menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

cost = 0.00
while True:
    
    try:
        item = input("input items: ").title()
        if item:
            for key, value in menu.items():
                if key == item:
                    cost += value
            print(f"Total: ${cost}")


    except EOFError:
        print("\n\n")
        print(f"Total: ${cost}")
        break

        

