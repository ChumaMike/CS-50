# separating two names with one AND
# three names with two commas and one AND
# and n names with n-1 commas and one AND, as in the below


names = "Adieu, adieu, to "
gamas = []
count = 0
while True:
    try:
        name = input("name: ").title()
        if name == 'Exit':  # Custom exit condition
            print(f"\n{names}")
            break
        
        if name and count == 0:
            names = "Adieu, adieu, to "
            names += name 
            gamas.append(name)
            
            count += 1
        elif name and count == 1:
            names = "Adieu, adieu, to "
            names += gamas[0] + " and " + name
            count += 1
            gamas.append(name)
            
        elif name and count == 2:
            names = "Adieu, adieu, to "
            names += gamas[0] + ", " + gamas[1] + ", " + "and " + name
            count+=1
        elif name and count > 2:
            names = "Adieu, adieu, to "
            for gama in gamas:
                names += gama + ", "
            names += "and" + name
            count+= 1
        else:
            pass
                        
    except EOFError:
        print()
        break