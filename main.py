import sys
from stats import num_words, letter_counter, report

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys,exit(1)
    text = get_text(sys.argv[1])
    word_counter = num_words(text)
    letter_count = letter_counter(text)
    character_report = report(letter_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_counter} total words")
    print("--------- Character Count -------")
    for i in character_report:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['num']}")
    print("============= END ===============")


def get_text(path):
    with open(path) as f:
        return f.read()

main()