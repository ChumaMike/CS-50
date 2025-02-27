try:
    expp = input("Arithmetic expression: ").strip()
    x, y, z = expp.split(" ")
    x = int(x)
    z = int(z)
    if y == "+":
        print(round(float(x + z), 1))
        
    elif y == "-":
        print(round(float(x - z), 1))

    elif y == "*":
        print(round(float(x * z), 1))

    elif y == "/":
        print(round(float(x / z), 1))
        
except:
    # print("Angazi ufakeni ndoda")
    print("hi")