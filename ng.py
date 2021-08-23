import random

n = random.randint(1.,99)
guess = int(input("Guess the number between 1-99: "))

while n != guess:
    if guess > n:
        print("Its higher than the number, guess otherone.")
        guess = int(input("Guess the number between 1-99: "))
    elif guess < n:
        print("Its lower than the number, guess otherone.")
        guess = int(input("Guess the number between 1-99: "))
if guess == n:
        print("Yes, it is!")