namee = input("camelCase: ")
""" firstName"""
name = ""
for cha in namee:
    if cha.isupper():
        name += "_" + cha.lower()
    else:
        name += cha
print(f"snake_case: {name}")