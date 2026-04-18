#Write a program to get 2 number from the user and display maximum number
print("To determine the maximum number")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if(a>b):
    print(a)
else:
    print(b)
print("The maximum value is "+str(max(a,b)))

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

# 1. Create an empty list
my_list = []

# 2. Prompt the user for five numbers
print("Please enter 5 numbers:")

for i in range(5):
    # We convert the input to a float so the user can enter decimals too
    num = float(input(f"Enter number {i+1}: "))
    my_list.append(num)

# 3. Print the list
print(f"\nYour list: {my_list}")

# 4. Analyze and print the results
print(f"Length of the list: {len(my_list)}")
print(f"Sum of all numbers: {sum(my_list)}")
print(f"Largest number: {max(my_list)}")
print(f"Smallest number: {min(my_list)}")