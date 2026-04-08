# to get 6 numbers
# store to list
# sum and display result to user
list = []
for i in range(6):
    list.append(int(input("Enter 6 number: ")))
print("These are the lists ")
print(list)
s = 0
for i in  list:
    s += i
print("Sum of the number in the  list is: " +str(s))

#clear the list
list = []
for i in range(6):
    list.append(int(input("Enter 6 number: ")))
print("These are the list of the 6 numbers")
print(list)
list.clear()
print("We have removed the list items: ")
print(list)

# Write a program to get 6 number in the tuple and display all number and then clear tuple and then display
tup = []
for i in range(6):
    tup.append(int(input("Enter 6 number: ")))
print("these are the list of the number: ")
print(str(tup))
print("The turple has been cleared")
tup.clear()
print(tup)

