while True:
    try:
        fraction = input("fraction: ")
        x, y = fraction.split("/")
        x, y = int(x), int(y)
        if y < x:
            raise ValueError
        else:
            percent = round(x/y * 100)

        if percent <= 1:
            print("E")
            break
        elif percent >= 99:
            print("F")
            break
        else:
            print(f"{percent}%")
            break
    except:
        print("Input not correct")

