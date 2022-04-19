def maximum(x, y, z):
    if x <= y >= z:
        print(y)
    elif y <= x >= z:
        print(x)
    else:
        print(z)
maximum(12, 32, 6)
