def word_count(text):
    splitted_text = text.split()
    return len(splitted_text)

def char_count(text):
    char_count = {}
    lower_text = text.lower()
    splitted_text = lower_text.split()
    joined_char = " ".join(splitted_text)
    for i in joined_char:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    return char_count

def sort_on(dict):
    return dict["count"]

def report(char_dict):
    chars_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            char_info = {'char': char, 'count': count}
            chars_list.append(char_info)
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list
