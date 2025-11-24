from stats import num_words, letter_counter

def main():
    path_to_file = "books/frankenstein.txt"
    text = get_text(path_to_file)
    word_counter = num_words(text)
    letter_count = letter_counter(text)
    print(letter_count)


def get_text(path):
    with open(path) as f:
        return f.read()

main()