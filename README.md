# BookBot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

A Python command-line tool that analyzes text files and generates statistical reports about word count and character frequency.

## Features

- Counts total words in a text file
- Analyzes character frequency (alphabetic characters only)
- Displays results sorted by frequency (most common first)
- Case-insensitive character counting

## Requirements

- Python 3.x

## Usage

```bash
python3 main.py <path_to_book>
```

**Example:**

```bash
python3 main.py books/frankenstein.txt
```

## Files

- `main.py` - Main program that handles command-line arguments and displays the report
- `stats.py` - Contains analysis functions for word counting and character frequency

## Output Format

The program displays:

1. The path to the analyzed file
2. Total word count
3. Character frequency (sorted from most to least common, alphabetic characters only)

**Sample Output:**

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 77986 total words
--------- Character Count -------
e: 46043
t: 30365
a: 26743
...
============= END ===============
```

## How It Works

1. Reads the entire text file
2. Counts words by splitting on whitespace
3. Counts each alphabetic character (case-insensitive)
4. Converts character counts to a sorted list
5. Displays results in a formatted report
