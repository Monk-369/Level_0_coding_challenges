def common_character(string_1, string_2):
    for letter in string_1:
        if letter in string_2:
            print(letter.lower(), end = ' ')
common_character('Bird', 'String')

