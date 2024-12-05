#Justin H Larsen
#09/24/2024
#P1HW2_LarsenJustin
#Program that does basic math

print("This program calculates and displays travel expenses")
print()

#asking for user's budget
user_budget = float(input("Enter your budget: "))

#asking user's destination
user_destination = str(input("Enter your travel destination: "))

#asking user how much they spent on gas
gas_cost = float(input("Enter total cost of fuel: "))

#ask user how much was spent on accommodations
accomm_cost = float(input("Enter total cost of accomodations: "))

#Ask user how much was spent on food
food_cost = float(input("Enter total cost of food: "))

#Add total cost of expenses
expense_total = (gas_cost + accomm_cost + food_cost)

#Subtract total expenses from budget
budget_diff =  (user_budget - expense_total)

#Display the results of the math above
print()
#print("--------------Travel Expenses-------------------")

#print(f"Location: {user_destination}")
#print(f"Initial Budget: {user_budget}")
#print()
#print()
#print(f"Fuel: {gas_cost}")
#print(f"Accommodations: {accomm_cost}")
#print(f"Food: {food_cost}")
#print()
#print()
#print(f"Remaining Balance: {budget_diff}")

#new hw version

print("--------------Travel Expenses-------------------")
print(f"{'Location:':<20} {user_destination}")
print(f"{'Initial Budget:':<20} ${user_budget:,.2f}")
print(f"{'Fuel:':<20} ${gas_cost:,.2f}")
print(f"{'Accomadation:':<20} ${accomm_cost:,.2f}")
print(f"{'Food:':<20} ${food_cost:,.2f}")
print("------------------------------------------------")
print()
print()
print(f"{'Remaining Balance:':<20} ${budget_diff:,.2f}")
