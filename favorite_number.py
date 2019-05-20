import json

number = input("What is your favorite number? \n")

filename = 'number.json'
with open(filename, 'w') as f_obj:
    json.dump(number, f_obj)
    print("Thank you. I shall never forget this.")
