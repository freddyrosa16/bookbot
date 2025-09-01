def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    characters = {}
    lower_text = text.lower()
    for key in lower_text:
        if key in characters:
            characters[key] += 1
        else:
            characters[key] = 1
    return characters

def character_report(text):
    new_dict = {}
    new_list = []
    character = character_count(text)
    for key, value in character.items():
        new_dict = {
            "char": key,
            "num": value
        }
        new_list.append(new_dict)
        new_list.sort(key=get_num, reverse=True)    
    return new_list

def get_num(item):
    return item["num"]
