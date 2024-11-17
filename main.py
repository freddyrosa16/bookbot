def main():
    path_to_file = "books/frankenstein.txt"
    text = read_story(path_to_file)
    counter = count_char(text)
    letter_count = letter_counter(text)
    repporting = report(letter_count, text)
    print(repporting)


def read_story(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def count_char(text):
    count = 0
    word = text.split()
    for i in word:
        count += 1
    return count


def letter_counter(text):
    new_dict = {}
    lower_string = text.lower()
    for key in lower_string:
        if key in new_dict:
            new_dict[key] += 1
        else:
            new_dict[key] = 1
    return new_dict


def report(letter_count, text):
    char_list = []
    for key, value in letter_count.items():
        char_list.append((key, value))
    char_list.sort(reverse=False)
    print("--- Begin report of books.frankestein.txt ---")
    print(f"{count_char(text)} words found in the document")
    print(" ")

    for key, value in char_list:
        if key.isalpha():
            print(f"The {key} character was found {value} times ")
    print("--- End report ---")


main()

