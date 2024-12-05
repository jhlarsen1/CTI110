'''
#Declare my variables
Declare String ename
Declare float hoursw, payr, overtimeh, overtimep, regularp, grossp,

#Request input from user
“Enter Employee's name: ”
“Enter number of hours worked: ”
“Enter employee's pay rate: ”

#Make Calculations
overtimeh = (hoursw - 40.0)
overtimep = (overtimeh * (payr * 1.5))
regularp = (hoursw * payr)
grossp = (overtimep + regularp)

#Display output/variables on one line in unison with descriptive string above the
#including if statements
if hours worked is greater than 40
    Calculate Ot hours worked by subtracting 40 from hours worked
    Calculate OT pay (overtimeh * (payr * 1.5))
    Calculate reg pay (40 * regular pay rate)
    Callculate grossp by adding overtimep + regularp

else (employee worked 40 hours or less)
    overtime hours = 0
    overtime pay = 0
    calculate reg pay by multiplying original hours worked by payr
    calculate gross pay is equal to regular pay

    

'''
#Request user input 
ename = input("Enter Employee's name: ")
hoursw = float(input("Enter number of hours worked: "))
payr = float(input("Enter employee's pay rate: "))

print("--------------------------------------------")
#Output variables and strings in line
print(f"Employee name: {ename}")
print()

if hoursw > 40:
    overtimeh = (hoursw - 40.0)
    overtimep = (overtimeh * (payr * 1.5))
    regularp = (40 * payr)
    grossp = (overtimep + regularp)

    print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'OverTime':<15}{'OverTime Pay':<20}{'RegHour Pay':<20}{'Gross Pay':<20}")
    print("-------------------------------------------------------------------------------------------------------------")
    print(f"{hoursw:<15}{payr:<15}{overtimeh:<15}{overtimep:<20}{regularp:<20}{grossp:<20}")

else:
    overtimep = 0
    overtimeh = 0
    regularp = (hoursw*payr)
    grossp = regularp

    print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'OverTime':<15}{'OverTime Pay':<20}{'RegHour Pay':<20}{'Gross Pay':<20}")
    print("-------------------------------------------------------------------------------------------------------------")
    print(f"{hoursw:<15}{payr:<15}{overtimeh:<15}{overtimep:<20}{regularp:<20}{grossp:<20}")

