def maximum(x, y, z):
    if x <= y >= z:
        print(y)
    elif y <= x >= z:
        print(x)
    else:
        print(z)
maximum('12', '32', '6')
#Bonus question
def infinite_numbers(*numbers):
    for number in numbers:
        print(number)
infinite_numbers('2', '2', '3', '7', '8', '9', '29', '11', '910', '92', '260')
