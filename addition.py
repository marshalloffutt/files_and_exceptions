# Provide user with break condition
print("Let's do some addition. Press 'q' at any time to quit. \n")

while True:
    try:
        # Get numbers to add from user input
        number_one = input("Provide a number: \n")

        # Check for break condition
        if number_one == 'q':
            break

        # Convert numbers to integers 
        number_one = int(number_one)

        number_two = input("Provide a second number: \n")
        if number_two == 'q':
            break
        
        number_two = int(number_two)

    # Throw ValueError exception if they provide anything not a number
    except ValueError:
        print("You are dumb. I asked for a number.")

    else:
        result = number_one + number_two
        print(str(number_one) + " + " + str(number_two) + " = " + str(result))