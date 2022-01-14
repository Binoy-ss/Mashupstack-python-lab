num = int(input(" number to divide: "))

a = list(range(1,num+1))

divisor = []

for number in a:
    if num % number == 0:
        divisor.append(number)

print(divisor)