def main():
    path = "books/frankenstein.txt"
    content = get_book(path)
    word_count = word_counter(content)
    letter_counts = letter_counter(content)
    print(letter_counts)


def get_book(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def word_counter(content):
    words = len(content.split())
    return words


def letter_counter(content):
    letter_counts = {}
    for letter in content.lower():
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    return letter_counts


main()
