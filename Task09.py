def vowel_finder(string):
    vowels = ('a' 'e' 'i' 'o' 'u' 'A' 'E' 'I' 'O' 'U')
    for letter in string:
        if letter in vowels:
            print(letter.lower(), end = ' ')
vowel_finder('Autumn')
