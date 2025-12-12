# 📚 BookBot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

BookBot is a simple command-line tool that analyzes a text file and prints a clear report with:

- Total word count
- Character frequency (case-insensitive, sorted by frequency)

This project is ideal for practicing Python, file I/O, and basic text processing.

## 🚀 Quickstart

Run the script from the command line:

```bash
python3 main.py <path_to_book>
```

Example:

```bash
python3 main.py books/frankenstein.txt
```

If no file path is provided, the script prints a usage message and exits.

## 🔧 What the code does

- `get_book_text(path)` — reads and returns the full text from a file path.
- `get_word_count(text)` — splits text on whitespace and returns a word count string (e.g. `Found 1234 total words`).
- `get_characters_count(text)` — lowercases the text and returns a dictionary mapping each character to its occurrence count.
- `get_report(characters)` — transforms the character-count dictionary into a list of `{"char": <char>, "num": <count>}` objects and sorts them by `num` descending.

## 🖨️ Example output

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt
----------- Word Count ----------
Found 78712 total words
--------- Character Count -------
a: 52100
e: 48722
t: 39218
...
============= END ===============
```

## 🛠️ Requirements

- Python 3.x

No external libraries required.

## 🧩 Notes & Suggestions

- `get_word_count` currently returns a formatted string. If you want to use the numerical value in code, change it to return an `int` instead of a string.
- `get_characters_count` counts every character (including whitespace and punctuation). If you only want alphabetical characters, filter with `str.isalpha()` before counting.
- Consider refactoring `get_report` to accept an optional `only_alpha=True` parameter to make filtering easier.
- There are indentation issues and unreachable code in `main()` in the provided script; you should move the logic that reads the file and prints the report into the top-level `main()` (inside the `if __name__ == "__main__":` guard) and ensure correct indentation.

## 🗂️ Suggested project layout

```
.
├── main.py      # CLI entry point
├── stats.py     # text-processing helpers (get_word_count, get_characters_count, get_report)
└── README.md
```

## 📄 License

This repository is provided for educational use. Feel free to adapt it for your projects.
