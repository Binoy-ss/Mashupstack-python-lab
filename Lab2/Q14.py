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