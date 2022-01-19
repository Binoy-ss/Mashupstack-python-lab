#Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.

import random

vowels = ['a','e','i','o','u']

for i in vowels:
    random.shuffle(vowels)
    print("".join(vowels))
