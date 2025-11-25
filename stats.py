def num_words(text):
    count = 0
    splitted_text = text.split()
    for i in splitted_text:
        count += 1
    return count

def letter_counter(text):
    character_counter = {}
    splitted_text = text.lower().split()
    for word in splitted_text:
        for letter in word:
            if letter in character_counter:
                character_counter[letter] += 1
            else:
                character_counter[letter] = 1
    return character_counter

def sort_on(items):
    return items["num"]

def report(characters):
    new_list = []
    for key, value in characters.items():
        new_dict = {
            "char": key,
            "num": value
        }
        new_list.append(new_dict)
    new_list.sort(reverse=True, key=sort_on)
    return new_list
        