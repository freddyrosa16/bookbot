import sys

from stats import get_book_text, get_character_count, get_count_word, stat_report


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    text = get_book_text(file_path)
    count = get_count_word(file_path)
    character_count = get_character_count(file_path)
    report_list = stat_report(file_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for dict in report_list:
        if dict["char"].isalpha():
            print(f"{dict['char']}: {dict['num']}")
    print("============= END ===============")


main()
