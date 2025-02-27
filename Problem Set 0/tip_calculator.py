def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


#format '$##.##'
def dollars_to_float(d):
    d = d.replace("$", "")
    return float(d)


def percent_to_float(p):
    p = p.replace("%", "")
    ans = int(p) /100
    return float(ans)


main()