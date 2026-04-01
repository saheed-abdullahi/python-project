print("Multiplication of number")
num = int(input("Enter number: "))
print("you entered "+str(num))
for i in range(0,13):
    print(str(i)+ " * " +str(num)+ " = " +str(i*num) )

#write a program to get 2 numbers from the user and display 2 table for the numbers
print("We are generating 2 tables in the section")
one= int(input("Enter the first number to generate table for: "))
second = int(input ("Enter the second number to genetate table for: "))
print("This is the table for " +str(one)+ " below")
for i in range(1,13):
    print(str(i)+ " * " +str(one)+ " = " +str(i*one))
print("This is the table for " +str(second)+ " below")
for i in range(1,13):
     print(str(i)+ " * " +str(second)+ " = "+str(i*second))
