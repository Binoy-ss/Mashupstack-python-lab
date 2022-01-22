#Write a Python program to find the index of an item of a tuple.
user_1 = tuple((input("enter elements : ")))

user_2 = input("enter the element of the input : ")

if user_2 in user_1:
    result = user_1.index(user_2)
    print("the index value of ",user_2," of your element is :",result)

else :
    print("index value not found")