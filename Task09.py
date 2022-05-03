def vowel_finder(string):
    vowel = []
    vowels = 'a''e''i''o''u'
    string = string.lower()
    for letter in set(string):
        if letter in vowels:
            vowel.append(letter)
    print(str(vowel))
vowel_finder('Autumn')
