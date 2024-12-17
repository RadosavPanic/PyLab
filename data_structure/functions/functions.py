def convert_text_underscore(text):
    """Converts input string to lowercase and replaces spaces into underscores and then returns given string."""
    underscore_string = text.lower().replace(" ", "_")
    return underscore_string


full_name_underscored = convert_text_underscore("John Doe")
print(full_name_underscored)  # john_doe


def append_list_items(list_to_update, items):
    """Appends individual item or list of items to given list"""
    if isinstance(items, list):
        for item in items:
            list_to_update.append(item)
    else:
        list_to_update.append(items)
    return list_to_update


numbers_list = [15, 41, 50]
append_list_items(numbers_list, 94)
print(numbers_list)  # [15, 41, 50, 94]
append_list_items(numbers_list, [38, 62, 33])
print(numbers_list)  # [15, 41, 50, 94, 38, 62, 33]

combine_and_dash = lambda text1, text2: (text1 + " " + text2).replace(" ", "-")
print(combine_and_dash("Python is a popular", "programming language"))  # Python-is-a-popular-programming-language