#Justin H Larsen
#11/15/2024
#P5LAB_LarsenJustin
#generate a random float at a self checkout machine

import random

def disperse_change(changeOwed):
    #Get money value from user as a float
    money = float(changeOwed)

    #Considering if the user put in 0.00
    if money == 0:
        print("No change")
        
    #Check for debt
    if money < 0:
        print("Ouch! You are in debt")
        money = 0
    #Convert money to a whole number
    money = round(money * 100)

    #print(money)

    #Calculate the amount of dollars in the money variable
    num_dollars = (money // 100)

    #print(f"Dollars: {num_dollars}")

    #Remove the dollars from money variable by re-assigning money
    money = money - (num_dollars * 100)

    #Calculate the amount of quarters
    num_quarters = (money // 25)

    #print(f"Quarters: {num_quarters}")

    #Remove the quarters from money variable by re-assigning money
    money = money - (num_quarters * 25)

    #Calculate the number of dimes
    num_dimes = (money // 10)

    #print(f"Dimes: {num_dimes}")

    #Remove the dimes from money variable by re-assigning money
    money = money - (num_dimes * 10)

    #Calculate the number of nickels
    num_nickels = (money // 5)

    #print(f"Nickels: {num_nickels}")

    #Remove the nickels from money variable by re-assigning money
    money = money - (num_nickels * 5)

    #Calculate the number of pennies
    num_pennies = money

    #print(f"Pennies: {num_pennies}")

    #print dollar amount gramattically correct
    if num_dollars > 0:
        if num_dollars ==1:
            print(f"{num_dollars} dollar")
        else: #variable is greater than one
            print(f"{num_dollars} dollars")
        
    #print dollar amount gramattically correct
    if num_quarters > 0:
        if num_quarters ==1:
            print(f"{num_quarters} quarter")
        else: #variable is greater than one
            print(f"{num_quarters} quarters")
        
    #print dollar amount gramattically correct
    if num_dimes > 0:
        if num_dimes ==1:
            print(f"{num_dimes} dime")
        else: #variable is greater than one
            print(f"{num_dimes} dimes")
    
    #print dollar amount gramattically correct
    if num_nickels > 0:
        if num_nickels ==1:
            print(f"{num_nickels} nickel")
        else: #variable is greater than one
            print(f"{num_nickels} nickels")
        
    #print dollar amount gramattically correct
    if num_pennies > 0:
        if num_pennies ==1:
            print(f"{num_pennies} penny")
        else: #variable is greater than one
            print(f"{num_pennies} pennies")




def main():
    moneyOwed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${moneyOwed}")
    cashPaid = float(input("How much will you put in the self-checkout? "))
    changeOwed = (cashPaid - moneyOwed)
    print(f"Change is: ${changeOwed:.2f}")
    print("")
    disperse_change(changeOwed)

if __name__ == "__main__":
    main()