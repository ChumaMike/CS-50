grosa = {
    
}
while True:
    try:
        item = input("Items: ").upper()
        if item:
            if item in grosa:
                grosa[item] += 1          
            else:
                grosa[item] = 1

    except EOFError:
        print("\n\n")
        break
for i in sorted(grosa):
    print(f"{grosa[i]} {i}")