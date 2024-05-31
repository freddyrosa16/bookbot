def main():
    path = "books/frankenstein.txt"
    content = get_book(path)
    print(content)


def get_book(path_to_file):
    with open(path_to_file) as f:
        return f.read()


main()
