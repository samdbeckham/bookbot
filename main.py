import sys
from stats import word_count
from stats import char_count
from stats import sort_chars

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def pretty_print(path, words, chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")

    for c in chars:
        char = c["char"]
        num = c["num"]
        if char.isalpha():
            print(f"{char}: {num}")

    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_contents = get_book_text(book_path)
    book_words = word_count(book_contents)
    book_chars = char_count(book_contents)
    sorted_chars = sort_chars(book_chars)

    pretty_print(book_path,book_words,sorted_chars)

main()

