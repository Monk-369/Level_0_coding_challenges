def maximum(num_1, num_2, num_3):
    if num_1 <= num_2 >= num_3:
        print(num_2)
    elif num_2 <= num_1 >= num_3:
        print(num_1)
    else:
        print(num_3)
maximum(12, 32, 6)
