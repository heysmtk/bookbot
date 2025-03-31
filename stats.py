def count_words(book):
    num_words = len(book.split())
    return num_words


def count_chars(content):
    char_num = {}  # Prázdný slovník pro počítání znaků

    for char in content:  # Procházíme každý znak přímo
        char = char.lower()  # Převedeme na malá písmena
        char_num[char] = char_num.get(char, 0) + 1  # Zvýšíme počet výskytů

    return char_num