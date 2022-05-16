def maximum_number(*list_1):
    max_num = list_1[0]
    for number in list_1:
        if number > max_num:
            max_num = number
    return max_num
print(maximum_number(12, 32, 6, 78, 90, 99, 877))

