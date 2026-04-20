def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def get_count_word(file_path):
    count = 0
    splitted_text = get_book_text(file_path).split()
    for i in splitted_text:
        count += 1
    return count


def get_character_count(file_path):
    character_count_dict = {}
    lower_characters = get_book_text(file_path).lower()
    for key in lower_characters:
        if key not in character_count_dict:
            character_count_dict[key] = 1
        else:
            character_count_dict[key] += 1
    return character_count_dict


def stat_report(file_path):
    report_list = []
    dict = get_character_count(file_path)
    for key, value in dict.items():
        new_dict = {"char": key, "num": value}
        report_list.append(new_dict)
    return report_list


def sort_on(items):
    return items["num"]
