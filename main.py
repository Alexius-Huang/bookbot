import sys
from stats import get_words_count, get_sorted_char_counts

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")    
    # print(get_book_text("./books/frankenstein.txt"))
    content = get_book_text(f"./{book_path}")

    print("----------- Word Count ----------")
    words_count = get_words_count(content)
    print(f"Found {words_count} total words")

    print("--------- Character Count -------")
    # print(get_char_counts(content))
    char_counts = get_sorted_char_counts(content)
    for char_count in char_counts:
        print(f"{char_count["char"]}: {char_count["num"]}")
    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

main()
