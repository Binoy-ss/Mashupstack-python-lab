#Write a python program to count repeated characters in a string.

userinput = input("Enter your input:")

count = {}

blank = userinput.replace(" ", " ")

for i in blank:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
repeated = { key: value for (key,value) in count.items() if value >=2}

print(repeated)


