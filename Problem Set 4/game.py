import random

while True:
    try:
        n = input("level: ")
        if int(n) > 0:
            n = int(n)
            x = random.randrange(1, n+1)
            while True:
                try:
                    guess = int(input("Guess: "))
                    if guess > 0:
                        if guess < x:
                            print("Too small!")
                        
                        elif guess > x:
                            print("Too large")
                        
                        elif guess == x:
                            print("Just right")
                            break
                    else:
                        pass
                except ValueError:
                    pass
            break
        else:
            pass
    except ValueError:
        pass