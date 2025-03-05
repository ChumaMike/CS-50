names = "Adieu, adieu, to "
gamas = []
count = 0

while True:
    try:
        name = input("name (or type 'exit' to quit): ").title()
        if name == 'Exit':  # Custom exit condition
            print(f"\n{names}.")
            break
        elif name:
            if count == 0:
                names = "Adieu, adieu, to "
                names += name
                gamas.append(name)
                count += 1
            elif count == 1:
                names += " and " + name
                count += 1
                gamas.append(name)
            elif count == 2:
                names += ", " + name
                count += 1
                gamas.append(name)
            elif count > 2:
                for gama in gamas:
                    names += ", " + gama
                names += " and " + name
                count += 1
    except Exception as e:
        print(f"Unexpected error: {e}")
