def read_pets(filename):
    """Print the names contained in the supplied filename"""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
            print(contents)
    except FileNotFoundError:
        pass

# Store the lists into a variable
filenames = ['text_files/cats.txt', 'text_files/dogs.txt']

for filename in filenames:
    read_pets(filename)