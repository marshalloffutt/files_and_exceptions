filename = 'guest_book.txt'

while True:
    name = input("What is your name? (press 'q' to quit)" + "\n")
    if name == 'q':
        break
    else:
         print("Hello " + name + ".")
         with open(filename, 'a') as file_object:
             file_object.write(name + "\n")
