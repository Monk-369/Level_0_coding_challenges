def maximum(num_1, num_2, num_3):
    if num_1 <= num_2 >= num_3:
        print(num_2)
    elif num_2 <= num_1 >= num_3:
        print(num_1)
    else:
        print(num_3)
maximum(12, 32, 6)
def maximum(*list_1):
    max_num = list_1[0]
    for number in list_1:
        if number > max_num:
            max_num = number
    return max_num
print(maximum(12, 32, 6, 78, 90, 99, 877))

