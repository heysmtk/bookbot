from stats import count_words, count_chars, sorted_chars
import sys

# Setting for CLI arguments
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(filepath):
    """Load and read the file"""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found!")
        sys.exit(1)


# Setting to variables
filepath = sys.argv[1]
text = get_book_text(filepath)
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