# Justin Larsen
# 9/17/2024
# P1HW1
# Input and output with mathematical expression

print ("-----Calculating Exponents----")
print ()
print ()

#Get base value (as an integer) from the user
base_value = int(input("Enter an integer as the base value: "))

#Get value (as an integer) to use as an exponent
exponent_value = int(input("Enter an integer as the exponent: "))

print ()
print ()

#Use base value and exponent value to calculate

result_value = base_value ** exponent_value

print(base_value, "raised to the power of", exponent_value, "is", result_value,"!!")

print ()
print ()

print ("----Addition and Subtraction----")

print ()
print ()

#Get a value(as an integer) to start with
starting_value = int(input("Enter a starting integer: "))

#Get a value(as an integer) for addition
second_value = int(input("Enter an integer to add: "))

#Get a value(as an integer) for subtraction
third_value = int(input("Enter an integer to subtract: "))

print ()
print ()

result_value2 = starting_value + second_value - third_value

print(starting_value,"+", second_value, "-", third_value, "is equal to", result_value2)
