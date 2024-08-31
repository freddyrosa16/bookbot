def main():
    path_to_file = "books/frankenstein.txt"
    reader = readers(path_to_file)
    word_count = counters(reader)
    letters = character_counter(reader)
    sorted_letters = sort_characters(letters)
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in the document")
    for char, count in sorted_letters:
        print(f"The {char} character was found {count} times")
    print("--- End report ---")


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
        if lowered.isalpha():
            if lowered not in character:
                character[lowered] = 1
            else:
                character[lowered] += 1
    return character


def sort_characters(character):
    character_list = list(character.items())
    character_list.sort()
    return character_list


main()
