# 🤖📚 BookBot

BookBot is a simple Python program that analyzes a text file (like a
novel) and generates a statistical report of its contents. It counts the
total number of words and shows how many times each character appears.

------------------------------------------------------------------------

## 🚀 Features

-   📖 Reads any `.txt` book file\
-   🔢 Counts total words\
-   🔤 Counts frequency of each character\
-   📊 Outputs a clean terminal report

------------------------------------------------------------------------

## 🛠️ How It Works

BookBot processes a text file and:

1.  Reads the full text
2.  Splits the text into words to count them
3.  Converts all characters to lowercase
4.  Counts how often each character appears
5.  Prints a formatted report

------------------------------------------------------------------------

## 📂 Project Structure

    bookbot/
    │── main.py
    │── stats.py
    │── books/
    │   └── example.txt

------------------------------------------------------------------------

## ▶️ Usage

Run the program from the command line:

``` bash
python3 main.py <path_to_book>
```

### Example:

``` bash
python3 main.py books/frankenstein.txt
```

------------------------------------------------------------------------

## 🧾 Example Output

    ============ BOOKBOT ============
    Analyzing book found at books/frankenstein.txt...
    ----------- Word Count ----------
    Found 78345 total words
    --------- Character Count -------
    a: 4567
    b: 1234
    c: 2345
    ...
    ============= END ===============

------------------------------------------------------------------------

## 🧠 Functions Overview

-   `get_book_text(path)` → Reads the file
-   `get_count_word(path)` → Counts total words
-   `get_character_count(path)` → Counts each character
-   `stat_report(path)` → Formats the character data

------------------------------------------------------------------------

## 📌 Notes

-   Only alphabetical characters are displayed in the final report
-   File must exist and be readable
