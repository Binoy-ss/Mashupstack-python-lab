import random

num = random.randrange(1, 10)

guess = int(input("Guess and Enter a number between 1 and 10 :"))


if guess == num:
    print("The Guess is correct")
elif guess < num:
    print("Try again. The Number was", num)
elif guess > num:
    print("Try again. The Number was", num)