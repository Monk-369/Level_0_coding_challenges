def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit
print(convert_to_fahrenheit(32), 'fahrenheit, is equal to 32 celsius')
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    return celsius
print(convert_to_celsius(89.6), 'celsius, is equal to 89.6 fahrenheit')
