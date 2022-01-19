import random

vowels = ['a','e','i','o','u']

for i in vowels:
    random.shuffle(vowels)
    print("".join(vowels))