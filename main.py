def main():
    path_to_file = "books/frankenstein.txt"
    reader = readers(path_to_file)
    print(reader)


def readers(path_to_file):
    with open(path_to_file) as f:
        return f.read()


main()
