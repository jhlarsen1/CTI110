#Justin Larsen
#10/31/2024
#P4LAB2
#Write a program that asks the user to enter an integer and display the multiplication table for that integer from 1 to 12. See example output below.

#While loop to control program running continuously
run_again = "y"

while run_again == "y":
    user_int = int(input("Enter an integer: "))
    if user_int >= 0:
        #print multiplication table
        for num in range(1,13):
            print(f"{user_int} * {num} = {user_int*num}")
    else:
        print("Cannot accept negative values")
    
    run_again = input("Would you like to run the program again?").lower()[0]
    while run_again != "y" and run_again != "n":
        print("invalid input must enter yes or no")
        run_again = input("Would you like to run the program again?").lower()[0]
#Loop breaks
print("Exiting Program...")