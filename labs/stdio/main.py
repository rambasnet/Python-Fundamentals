"""
    StdIO Lab
    ASCII Art - using literals and variables
    
    Updated By: <Your name> #FIXME1
    Date: ... #FIXME2
    
    This program produces an ASCII art on the console.

    Algorithm steps: 
    1. Use variables to store data/values
    2. Write a series of print statements to print the data/values to the console
"""

print("Welcome to ASCII Art Program...\n")

# FIXME3: prompt user to enter their name and store the value into name variable using input function
# FIXME4: greet the name using the variable as the following output
# must output: Nice meeting you, <name>!

# prompt user to enter the semester and store the value into semester variable using input function
semester: str = input("What semester is this [Fall/Spring]? ")
print("This is " + semester + " semester.\n")

# FIXME5: prompt user to enter the year and store the value into year variable using input function
# FIXME6: print the year using the variable as the following output
# must output: This is <year> year.

print("Hope you like my ASCII art...\n\n")

line1: str = "  |\\_/|   **********************    (\\_/)\n"
print(line1)

# FIXME7: use variable to print the second line of the graphic
# FIXME8: print the third line of the graphics
# FIXME9: use variable to print the fourth line
# FIXME10: use variable to print the fifth line
# Note: You can add more lines or print more ASCII arts of your choice if you'd like...

print("\nGood bye...  \n")
