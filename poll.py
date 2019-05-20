filename = 'poll_responses.txt'

while True:
    response = input("Why do you like programming? (press 'q' to quit)" + "\n")
    if response == 'q':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(response + "\n")