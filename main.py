def main():
    path = "books/frankenstein.txt"
    content = get_book(path)
    word_count = word_counter(content)
    letter_counts = letter_counter(content)
    print_report(path, word_count, letter_counts)


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


def print_report(path, word_count, letter_counts):
    sorted_letter_counts = sorted(
        letter_counts.items(), key=lambda item: item[1], reverse=True)
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")
    for char, count in sorted_letter_counts:
        if char.isalpha():  # Only print alphabetic characters
            print(f"The '{char}' character was found {count} times")
    print("--- End report ---")


if __name__ == "__main__":
    main()
