# Prompt user for two numbers
try:
    number_one = int(input("Provide a number. \n"))
    number_two = int(input("Provide a second number. \n"))

# Catch exception if they provide a non-number
except ValueError:
    print("You are dumb. I said to provide a number.")

# Print the result of addition
else:
    result = number_one + number_two
    print(str(number_one) + " + " + str(number_two) + " = " + str(result))
