def area_of_triangle(num_1, num_2, num_3):
    semiperimeter = 0.5 * (num_1 + num_2 + num_3)
    area = (semiperimeter * (semiperimeter - num_1) * (semiperimeter - num_2) * (semiperimeter - num_3)) ** 0.5
    return area
print(area_of_triangle(9, 13, 6))
