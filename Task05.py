def area_of_triangle(x, y, z):
    s_p = 0.5 * (x + y + z)
    area = (s_p * (s_p - x) * (s_p - y) * (s_p - z)) ** 0.5
    return area
area_of_triangle('3', '4', '5')
