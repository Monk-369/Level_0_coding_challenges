def common_character(string_1, string_2):
    common_chars = []
    string_1 = string_1.lower()
    string_2 = string_2.lower()
    for letter in string_1:
        if letter in string_2:
            common_chars.append(letter)
    print(str(common_chars).lower())
common_character('BiRd', 'String')
