# First Name: Matthew, Last Name: Rude, Student ID: #001260851
from CLI import *

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Main function that runs the project
if __name__ == '__main__':
    # Create a user_input loop to act as a command line interface
    # Algorithmic Complexity: O(n^3)
    # Infinite while loop to gather user input, beaks when user types x or X
    while True:
        # Gather user input from command line interface and put it into a variable called user_input
        user_input = input("Please enter a valid time in military time format ie. '1600' or enter 'X' to end the "
                           "program.")

        # If user input is x, end the application.
        if user_input == "X" or user_input == "x":
            print("Program closed.")
            # Break while loop if user enters x or X
            break
        # If the user input is a valid military time... process the time and return package/delivery info
        elif validate_input(user_input):
            process_time(user_input)
