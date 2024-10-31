import random

random_number = random.randint(1, 100)
for i in range(5):
    guess = int(input("guess number (1-100): "))
    if guess > random_number:
        print("Too High, Try again")
    elif guess < random_number:
        print("Too Low, Try again")
    else:
        print("Winnn !")
        break
else:
    print("lose")
