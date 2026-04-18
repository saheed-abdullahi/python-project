# #Write a python program to get 5 number from user in array and sum all number and display
# import array as arr
# a= arr.array("i", [])
# s= 0
# for i in range(5):
#     a.append(int(input("Enter a number to store in the array: ")))
# for j in range(5):
#     print(a[j])
#     s += a[j]
# print("sum of the number is:" +str(s))

#Write a pyton program to get 5 number from the user in array, and find maximum number
import array as arr
b = arr.array("i", [])
for i in range(5):
    b.append(int(input("Enter a number to store in the array: ")))
   
for j in range(5):
    print(b[j])
print("The maximum value is: " +str(max(b)))