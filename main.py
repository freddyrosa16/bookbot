def main():
    path_to_file = "books/frankenstein.txt"
    reader = readers(path_to_file)
    word_count = counters(reader)
    letters = character_counter(reader)
    print(letters)


def readers(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def counters(reader):
    words = reader.split()
    return len(words)


def character_counter(reader):
    character = {}
    for c in reader:
        lowered = c.lower()
        if lowered not in character:
            character[lowered] = 1
        else:
            character[lowered] += 1
    return character


main()
