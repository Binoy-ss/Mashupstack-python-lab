import random

UPPERCASE = "QWERTYUIOPASDFGHJKLZXCVBNM"
lowercase = "qwertyuiopasdfghjklzxcvbnm"
Numbers = "1234567890"
Symbols = "!@#$%^&*()_+="

add = UPPERCASE + lowercase + Numbers + Symbols
length = 8
password = "".join(random.sample(add , length))
print("Auto generated password is:", password)


