#Write a Python program to sum all the items in a list.

list = [1,2,3,4,5]
sum = 0
for i in range(len(list)):
	sum += list[i]
print(sum)