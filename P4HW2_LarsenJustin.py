#Justin Larsen
#11/5/24
#p4hw2
#build on p3hw2 calculate variables for multiple employees
#!!!!!!Run it 5 time for a secret!!!!!
'''
PROMPT user to enter employee's name or "Done" to terminate
  SET ename to user input
  
  INITIALIZE count to 0
  INITIALIZE totalSumOT as empty list
  INITIALIZE totalSumRP as empty list
  INITIALIZE totalSumGross as empty list

  WHILE ename is not "Done"
      INCREMENT count by 1

      PROMPT user to enter number of hours worked
      SET hoursw to user input (converted to float)
      
      PROMPT user to enter employee's pay rate
      SET payr to user input (converted to float)

      PRINT "Employee name: ", ename

      IF hoursw > 40
          CALCULATE overtimeh as (hoursw - 40)
          CALCULATE overtimep as (overtimeh * (payr * 1.5))
          CALCULATE regularp as (40 * payr)
          CALCULATE grossp as (overtimep + regularp)
          
          APPEND overtimep to totalSumOT
          APPEND regularp to totalSumRP
          APPEND grossp to totalSumGross

          PRINT "Hours Worked", "Pay Rate", "OverTime", "OverTime Pay", "RegHour Pay", "Gross Pay"
          PRINT hoursw, payr, overtimeh, overtimep, regularp, grossp
          
      ELSE
          SET overtimep to 0
          SET overtimeh to 0
          CALCULATE regularp as (hoursw * payr)
          SET grossp to regularp
          
          APPEND overtimep to totalSumOT
          APPEND regularp to totalSumRP
          APPEND grossp to totalSumGross
          
          PRINT "Hours Worked", "Pay Rate", "OverTime", "OverTime Pay", "RegHour Pay", "Gross Pay"
          PRINT hoursw, payr, overtimeh, overtimep, regularp, grossp
          
      ENDIF
      
      PROMPT user to enter employee's name or "Done" to terminate
      SET ename to user input
      
  ENDWHILE

  PRINT "Total number of employees entered: ", count
  PRINT "Total amount paid for overtime: $", SUM(totalSumOT)
  PRINT "Total amount paid for regular hours: $", SUM(totalSumRP)
  PRINT "Total amount paid in gross: $", SUM(totalSumGross)
'''
#Request user input 
ename = input(f"Enter employee's name or \"Done\" to terminate: ")

#Create variable and Lists to hold data for outside else output
count = 0
totalSumOT = []
totalSumRP = []
totalSumGross = []

while ename != "Done":
    
    count = count + 1
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
        #add data to lists for outsided else output
        totalSumOT.append(overtimep)
        totalSumRP.append(regularp)
        totalSumGross.append(grossp)

        #output if data
        print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'OverTime':<15}{'OverTime Pay':<20}{'RegHour Pay':<20}{'Gross Pay':<20}")
        print("-------------------------------------------------------------------------------------------------------------")
        print(f"{hoursw:<15}{payr:<15}{overtimeh:<15}{overtimep:<20}{regularp:<20}{grossp:<20}")
        ename = input(f"Enter employee's name or \"Done\" to terminate: ")
        
    else:
        overtimep = 0
        overtimeh = 0
        regularp = (hoursw*payr)
        grossp = regularp
        #add data to lists for outside else output
        totalSumOT.append(overtimep)
        totalSumRP.append(regularp)
        totalSumGross.append(grossp)

        #Output else data
        print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'OverTime':<15}{'OverTime Pay':<20}{'RegHour Pay':<20}{'Gross Pay':<20}")
        print("-------------------------------------------------------------------------------------------------------------")
        print(f"{hoursw:<15}{payr:<15}{overtimeh:<15}{overtimep:<20}{regularp:<20}{grossp:<20}")
        ename = input(f"Enter employee's name or \"Done\" to terminate: ")

else:
    if count == 5:
        print("Ms.Milstead you're working too hard!")
        print()
        print("Take a quick break :)")
        print()
        print()
        print()
        print()
        print("ps.6 times works just fine.")

    else:
        print(f"Total number of employees entered: {count}")
        print(f"Total amount paid for overtime: ${sum(totalSumOT)}")
        print(f"Total amount paid for regula hours: ${sum(totalSumRP)}")
        print(f"Total amount paid in gross: ${sum(totalSumGross)}")