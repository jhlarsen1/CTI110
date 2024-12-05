#Justin H Larsen
#10/03/2024
#P2LAB1
#tests knowledge of how to write code that uses a dictionary

#Create Dictionary
vehicles_and_mpg = {"Camaro":18.21, "Prius":52.36, "Model S":110, "Silverado":26}


#Print Dictionary Keys
#.keys() is a function that creates a list of the keys
keys = vehicles_and_mpg.keys()
print(keys)
print()


#Request user input for name of a vehicle from dictionary
user_input = input("Enter a vehicle from key above to see it's mpg(input is case sensitive): ")
print()


#Save the value as a variable
gas = vehicles_and_mpg[user_input]


#Display the MPG for
print(f"The {user_input} gets {gas} mpg")
print()


#Prompt the user to enter the number of miles that they will drive the vehicle
distance = float(input(f"How many miles will you drive the {user_input}? "))
print()


#Calculate the gallons of gas needed to drive the specified vehicle the given number of miles.
gas_needed = distance / gas
print(f"{gas_needed:.2f} gallon(s) of gas are needed to drive the {user_input} {distance} miles.")

