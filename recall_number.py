import json

def recall_number():
    """Recall the user's favorite number"""
    filename = 'number.json'

    try:
        with open(filename) as f_obj:
            number = json.load(f_obj)

    except FileNotFoundError:
        number = input("What is your favorite number? ")
        with open(filename, 'w') as f_obj:
            json.dump(number, f_obj)
            print("Thank you. I shall never forget this.")

    else:
        print("I know your favorite number! It's " + str(number) + ".")


recall_number()