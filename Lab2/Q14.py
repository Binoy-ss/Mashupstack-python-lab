#Write a Python program to remove an item from a set if it is present in the set.
userinput = int(input("Enter set:"))

list = list (())

for i in range (userinput):
    list.append(input("Enter Your list :"))
print(list)



user = input("Enter set to be removed:")
if user in list:
  list.remove(user)
  print(list)

else:

 print("item not found !!!")
