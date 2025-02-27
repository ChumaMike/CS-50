
def is_valid(vanity):
    puncs = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    gamaa = ""
    for word in vanity:
        if word.isdigit():
            gamaa += word
        elif word in puncs:
            return False
    if gamaa.startswith("0"):
        return False
    if 2 < len(vanity) < 7 and (vanity[-1].isdigit()):
        return True
    else:
        return False


def main():
    plate = input("Vanity plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

main()