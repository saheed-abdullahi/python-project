#Write a program to get 2 number from the user and display maximum number
# print("To determine the maximum number")
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# if(a>b):
#     print(a)
# else:
#     print(b)
# print("The maximum value is "+str(max(a,b)))

#Write a program to get 3 number from the user and display the maximum number
d=int(input("Enter the first number: "))
e=int(input("Enter the second number: "))
f= int(input("Enter the third number: "))
if(d>e>f):
    print(str(d)+ " is the maximum value")
elif(e>d>f):
    print(str(e)+ " is the maximum value")
else:
    print(str(f)+ " is the maximum value")