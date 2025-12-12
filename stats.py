def get_word_count(text):
    count = 0
    words = text.split()
    for word in words:
        count += 1
    return f"Found {count} total words"

def get_characters_count(text):
    character_count = {}
    word = text.lower()
    for character in word:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count

def get_report(characters):
    report_list = []
    for key, value in characters.items():
        report_dict = {
            "char": key,
            "num": value
        }
        report_list.append(report_dict)
    report_list.sort(reverse=True, key=sort_on)
    return report_list


def sort_on(items):
    return items["num"]