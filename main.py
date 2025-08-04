from stats import count_words, count_chars, sort_characters, display_stats

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    book_path = "books/frankenstein.txt"
    book = get_book_text(book_path)
    word_count = count_words(book)

    character_count = count_chars(book)
    character_list = sort_characters(character_count)
    display_stats(book_path, word_count, character_list)



main()