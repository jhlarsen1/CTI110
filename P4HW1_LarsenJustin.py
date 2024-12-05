#Justin H Larsen
#11/5/24
#p4hw1
#Ask user amount of scores, input scores, and validate data

'''
Declare List gradeList
Declare int scoreCount, count
Declare float gradeInput

Create List for user input

Input = Display "How many scores do you want to enter?"
for loop in the range of scoreCount

Input = Display"Enter score"(+1  to variable because python starts at 0)

Use While loop to validate data
gradeInput < 0 or gradeInput > 100
Display "INVALID Score entered!!!!"
Display "Score should be between 0 and 100"

Set calculations for avg

Display Lowest grade
Display List with Lowest grade removed
Display the average  of the grades

If statement to reasign grade as a letter grade
    Display Letter grade based on a average

'''

#create list to hold user inputs
gradeList = []

#Get input for how many times loop will run
scoreCount = int(input("How many scores do you want to enter? "))

#create a loop that uses above variable to control how many inputs user enters
for count in range(scoreCount):
    
    #get user input for the grade
    gradeInput = float(input(f"Enter score #{count+1} "))
    
    #validate the input
    while 0.0 > gradeInput or gradeInput > 100.0:
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        gradeInput = float(input(f"Enter score #{count+1} "))
    
    #inside for loop add grades to list
    gradeList.append(gradeInput)

print()
print()
#print results, lowest, modified list, average, and letter grade
print("---------------Results---------------")
print(f"Lowest Score : {min(gradeList)}")
gradeList.remove(min(gradeList))
print(f"Modified List : {[gradeList]}")
gradeAvg = sum(gradeList) / len(gradeList)
print(f"Scores Average : {gradeAvg:.2f}")
if gradeAvg >= 90:
    gradeAvg = "A"
elif gradeAvg >= 80:
    gradeAvg = "B"
elif gradeAvg >= 70:
    gradeAvg = "C"
elif gradeAvg >= 60:
    gradeAvg = "D"
else:
    gradeAvg = "F"
print(f"Grade : {gradeAvg}")