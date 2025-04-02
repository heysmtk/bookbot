def count_words(book):
    num_words = len(book.split())
    return num_words


def count_chars(content):
    char_num = {}  
    for char in content:  
        char = char.lower()  
        char_num[char] = char_num.get(char, 0) + 1
    return char_num


def sorted_chars(data):
    items = list(data.items())
    items.sort(key=lambda item: item[1], reverse=True)
    sorted_data = dict(items)
    return sorted_data