def main():
    path_to_file = "books/frankenstein.txt"
    reader = readers(path_to_file)
    word_count = counters(reader)
    print(reader)
    print(f"{word_count} words found in the document.")


def readers(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def counters(reader):
    counter = 0
    words = reader.split()
    for word in words:
        counter += 1
    return counter


main()
