from stats import count_words, count_chars

def get_book_text(filepath):
    """Load and read the file"""
    with open(filepath, "r") as file:
        content = file.read()
    return content


text = get_book_text("books/frankenstein.txt")

number_of_words = count_words(text)
print(f"{number_of_words} words found in the document")

number_of_characters = count_chars(text)
print(number_of_characters)