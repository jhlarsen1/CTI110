#Justin H Larsen
#10/8/2024
#P2HW2_LarsenJustin
#store the grades entered in a list
#Display list as seperate variables

#Declare Variable
#Declare Real mod1grade mod2grade mod3grade mod4grade mod5grade mod6grade
#Calculations
#lowgrade = min(user_grades)
#highgrade = max(user_grades)
#sumgrade = sum(user_grades)
#avggrade = sum(user_grades) / 6

#create a list
user_grades = []

#create input statements for grades
mod1grade = float(input(f"Enter grade for Module 1: "))
user_grades.append(mod1grade)
mod2grade = float(input(f"Enter grade for Module 2: "))
user_grades.append(mod2grade)
mod3grade = float(input(f"Enter grade for Module 3: "))
user_grades.append(mod3grade)
mod4grade = float(input(f"Enter grade for Module 4: "))
user_grades.append(mod4grade)
mod5grade = float(input(f"Enter grade for Module 5: "))
user_grades.append(mod5grade)
mod6grade = float(input(f"Enter grade for Module 6: "))
user_grades.append(mod6grade)
print()
print()
print("------------Results------------")

#create variables and logic for contents of list
lowgrade = min(user_grades)
highgrade = max(user_grades)
sumgrade = sum(user_grades)
avggrade = sum(user_grades) / 6


#print the variables created from the list
print(f"{'Lowest Grade:':<20} {lowgrade:.2f}")
print(f"{'Highest Grade:':<20} {highgrade:.2f}")
print(f"{'Sum of Grades:':<20} {sumgrade:.2f}")
print(f"{'Average':<20} {avggrade:.2f}")


print("----------------------------------------")
