import sys
from stats import get_word_count, get_characters_count, get_report

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]
    text = get_book_text(path_to_file)
    word = get_word_count(text)
    characters = get_characters_count(text)
    report = get_report(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}")
    print(f"----------- Word Count ----------")
    print(f"{word}")
    print("--------- Character Count -------")
    for r in report:
        if r["char"].isalpha():
            print(f"{r['char']}: {r['num']}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()