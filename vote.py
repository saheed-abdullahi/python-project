# Write a python program to take age from the user to check whether user able to 
# participate in voting or not. if age is less than 18 then it does't allow to 
# participate. and show , after how much year a person will be able to participate
# in voting
# Expected result if user input 10 years then:
# sorry! you cannot participate in voting, you will be able to participate after 8 year
name = input("Enter your name: ")
age = int(input("Enter your age: "))
if (age>=18):
    print ("Hi "+name+ " you can take part in the election")
else:
    print( "hi " +name+" you cannot participate in the election because your age is "+str(age)+ "years, you will wait for " +str(18-age)+ " year")
