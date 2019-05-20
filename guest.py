# Store file into a variable
filename = 'guest.txt'

# Prompts the user for their name
name = input("What is your name? ")

# Read
with open(filename, 'w') as file_object:
    file_object.write(name)