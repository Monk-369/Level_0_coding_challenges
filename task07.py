def convert(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit
print(convert(32), 'fahrenheit')
def convert(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    return celsius
print(convert(89.6), 'celsius')
