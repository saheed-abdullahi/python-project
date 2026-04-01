#Write a program to get 6 subject marks from the user and calculate total and avarage of the marks. and dispay to user
print("Finding the total and average of six subject")
first_sub = int(input("Enter your  scorce in first subject: "))
second_sub = int(input("Enter your  scorce in second subject: "))
third_sub = int(input("Enter your  scorce in third subject: "))
fourth_sub = int(input("Enter your  scorce in fouth subject: "))
fifth_sub = int(input("Enter your  scorce in fifth subject: "))
sixth_sub = int(input("Enter your  scorce in first subject: "))
total = first_sub+second_sub+third_sub+fourth_sub+fifth_sub+sixth_sub
print("The total scorce for all subject is : "+str(total))
average= total/600
print("The average of all scorces is : "+str(average))


#Write a program to get 6 subject marks from the user and calculate total,average and percentage
print("Calculating the the total marks, average and percentage")
a= int(input("Enter the first mark: "))
b= int(input("Enter the second mark: "))
c=int(input("Enter the third mark: "))
d=int(input("Enter the fouth mark: "))
e=int(input("Enter the fifth mark: "))
f = int(input("Enter the sixth mark: "))
g= a+b+c+d+e+f
print("This is the total: "+str(g))
h= int(input("Enter the total average of the six subject: "))
ave= g/h
print("The average for the Six subject is : "+str(ave))
percentage=ave/100
print("The percentage of the total scorce is : "+str(percentage))


