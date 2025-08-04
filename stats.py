def count_words(file_contents):
    by_words = file_contents.split()
    word_count = len(by_words)
    return word_count

def count_chars(file_contents):
    lower_case = file_contents.lower()
    char_count = {}
    for char in lower_case:
        char.lower()
        if char in char_count:
            char_count[char] = char_count[char] + 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(items):
    return items["num"]

def sort_characters(char_count):
    dictionary_list = []
    for key in char_count:
        new_dictionary = {"letter":key, "num": char_count[key]}
        dictionary_list.append(new_dictionary)
        dictionary_list.sort(key=sort_on,reverse=True)
    return dictionary_list

def display_stats(book_path, word_count, character_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for letter in character_list:
        if not letter["letter"].isalpha():
            continue
        else:
            print(f"{letter["letter"]}: {letter["num"]}")
    print("============= END ===============")
    
