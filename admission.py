# write A python program to take marks from the user to check whether user able to grant 
# admission in college or not. if marks is less than 60 then it don't allow to take
#  admission 
name = input("Enter your name: ")
score = int(input('Enter your scores: '))
if(score >= 60):
    print("congratulations! " +name+ " you are grant for the admission to our college(college of health)")
else:
    print("sorry fellow applicant," +name+ ", your score is "+str(score)+ " and it is less than our cut of mark. you need " +str(60-score)+ " to allow for the addmission")
    