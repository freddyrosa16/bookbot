def main():
    path = "books/frankenstein.txt"
    content = get_book(path)
    word_count = word_counter(content)
    print(f"The're are {word_count} in the book.")


def get_book(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def word_counter(content):
    words = len(content.split())
    return words


main()
