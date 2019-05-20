# Store file into a variable
filename = 'learning_python.txt'

# Read entire file
with open(filename) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

print("\n")

# Read line by line
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

print("\n")

# Make a list of lines from file
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())

print("\n")

# Replace Python for C
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.replace('Python', 'C')
    print(line.rstrip())