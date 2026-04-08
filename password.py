#write python program to get password from user and make sure that the password should contain number and alphabet
password = input("Enter your password: ")
if(password.isalnum()):
    print("your password is: "+password)
else:
    print("The password should be in letters and numbers")


#Write python program to get password from user and make sure the password should contain number and alphaberic
#and password length should not be greater than or equal to 8
pwd = input("Enter your password: ")
if len(pwd)>=8:
    print("The password is: "+str(pwd))
elif len(pwd)<8:
    print("The password must reaches 8 character")
if(pwd.isalnum()):
    print("your password is: "+pwd)
else:
    print("Error, the password should be alpbetical and numerical value only")