from stats import count_words, count_chars, sort_characters, display_stats
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        book = get_book_text(book_path)
        word_count = count_words(book)

        character_count = count_chars(book)
        character_list = sort_characters(character_count)
        display_stats(book_path, word_count, character_list)



main()