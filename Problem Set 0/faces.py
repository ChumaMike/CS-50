def convert(sente):
    sente = sente.replace(":)", "🙂")
    sente = sente.replace(":(", "🙁")
    return sente
def main():
    anosente = input("Wass good? ")
    print(convert(anosente))

main()


