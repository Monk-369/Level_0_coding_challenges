def convert(celsius):
    temperature = celsius
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit
#print(convert('add value'), 'fahrenheit')

def convert(fahrenheit):
    temperature = fahrenheit
    celsius = (fahrenheit - 32) / 1.8
    return celsius
#print('add value'), 'celsius')
