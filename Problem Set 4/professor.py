import random

def main():
    count = 0
    correct = 0
    fail = 0
    level = get_level()
    for i in range(10):
        num1 = generate_integer(level)
        num2 = generate_integer(level)
        
        while True:
            try:
                if count == 3:
                    fail += 1
                    print(num1 + num2)
                    count = 0
                    break
                
                ask = input(str(num1) + " + " + str(num2) + " = ")
                if ask.isdigit() and int(ask) == (num1 + num2):
                    correct += 1
                    count = 0
                    break
                else:
                    count += 1
                    print("EEE")
                    pass
            except ValueError:
                pass
    print(f"Correct: {correct} and Incorrect: {fail}")
    


def get_level():
    levels = "123"
    while True:
        try:
            n = input("level: ")
            if n in levels:
                return n
                break
            
        except Exception as e:
            print(f"Something wrong happened, {e}")
        
    

def generate_integer(level):
    if level == "1":
        return random.randint(1, 9)
    elif level == "2":
        return random.randint(10, 99)
    elif level == "3":
        return random.randint(100, 999)
    else:
        raise ValueError
        


if __name__ == "__main__":
    main()



