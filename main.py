import sys
from stats import get_count_words, get_count_characters, get_report

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    word_count = get_count_words(text)
    character_count = get_count_characters(text)
    report = get_report(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for r in report:
        if r['char'].isalpha():
            print(f'{r["char"]}: {r["num"]}')
    print("============= END ===============")
    


def get_book_text(path):
    with open(path) as file:
        return file.read()
    
main()