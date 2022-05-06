def vowel_finder(string):
    vowels_matched = []
    vowels = 'a''e''i''o''u'
    string = string.lower()
    for letter in set(string):
        if letter in vowels:
            vowels_matched.append(letter)
    print(', '.join(vowels_matched))
vowel_finder('Autumn')

