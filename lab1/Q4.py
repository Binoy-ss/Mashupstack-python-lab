a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


c = sorted(list(set(a) | set(b)))

print("The First List is :", a, ".")
print("The Second List is :", b, ".")
print("The New list without duplicates:", c, ".")