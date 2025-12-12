📚 BookBot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

BookBot is a simple command-line tool that analyzes a text file and reports:

Total word count

Character frequency (case-insensitive and sorted by most frequent)

This project is ideal for practicing Python, file I/O, and basic text processing.

🚀 How It Works

BookBot takes the path to a .txt file as a command-line argument, reads its contents, and prints a formatted analysis report.

Features

Count the total number of words

Count occurrences of each character (letters only)

Sort characters by frequency

Output a clear, structured report in the terminal

📦 Usage

Run the script from the command line:

python3 main.py <path_to_book>

Example:

python3 main.py books/frankenstein.txt

If no file path is provided, the script displays a usage message.

🧠 Functions Overview
get_word_count(text)

Splits the text by whitespace and returns the total number of words.

get_characters_count(text)

Converts text to lowercase and counts occurrences of each character.

get_report(characters)

Converts the character dictionary into a list of {char, num} objects and sorts them by frequency.

get_book_text(path)

Reads and returns the full text of the file.

🖨️ Example Output
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

🛠️ Requirements

Python 3.x

No external dependencies are required.

📁 Project Structure
.
├── main.py
├── stats.py
└── README.md

📄 License

This project is for educational purposes, inspired by the BookBot exercises from boot.dev.
