def common_words(filename, word):
    """Count the number of times a specific word appears"""
    try:
        with open(filename, encoding='utf-8') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        message = "Sorry, the file " + filename + " was not found."
        print(message)
    else:
        # Count the number of times a specific word was used
        count = contents.count(word.lower())
        print("The word " + word + " appears " + str(count) + " times in this text.")

# Call common_words and pass it in the arguments
common_words('text_files/lorem.txt', 'ipsum')
common_words('text_files/lorem.txt', 'ridiculus')
common_words('text_files/lorem.txt', 'fringilla')
