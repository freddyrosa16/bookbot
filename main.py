def main():
    path_to_file = "books/frankenstein.txt"
    reader = readers(path_to_file)
    word_count = counters(reader)
    letters = character_counter(reader)
    print(reader)
    print(f"{word_count} words found in the document.")
    print(letters)


def readers(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def counters(reader):
    words = reader.split()
    return len(words)


def character_counter(reader):
    character = {}
    lower_string = reader.lower()
    for i in lower_string:
        if i not in character:
            character[i] = 1
        else:
            character[i] += 1
    return character


main()
