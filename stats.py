def get_count_words(text):
    words = text.split()
    return len(words)

def get_count_characters(text):
    character_count = {}
    lower_text = text.lower()
    for letter in lower_text:
        if letter in character_count:
            character_count[letter] += 1
        else:
            character_count[letter] = 1
    return character_count

def get_report(character_count):
    new_report = []
    for key, value in character_count.items():
        new_dict = {
            "char": key,
            "num": value
        }
        new_report.append(new_dict)
    new_report.sort(reverse=True, key=sort_on)
    return new_report

def sort_on(items):
    return items["num"]