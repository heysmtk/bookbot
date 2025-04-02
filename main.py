from stats import count_words, count_chars, sorted_chars

def get_book_text(filepath):
    """Load and read the file"""
    with open(filepath, "r") as file:
        content = file.read()
    return content


# Setting to variables
filepath = "frankenstein.txt"
text = get_book_text(f"books/{filepath}")
number_of_words = count_words(text)
number_of_characters = count_chars(text)
sorted_characters = sorted_chars(number_of_characters)

result = ""
for char, count in sorted_characters.items():
    if char.isalpha():
        result += f"{char}: {count}\n"

# Priting the report
print("============ BOOKBOT ============")
print(f"Analyzing book found at books/{filepath}...")
print("----------- Word Count ----------")
print(f"Found {number_of_words} total words")
print("--------- Character Count -------")
print(result)
print("============= END ===============")