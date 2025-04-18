from stats import word_count, char_count, report
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]

def main():
    text = get_book_text(book_path)
    count = word_count(text)
    char = char_count(text)
    rep = report(char)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for char_dict in rep:
        print(f"{char_dict['char']}: {char_dict['count']}")
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()