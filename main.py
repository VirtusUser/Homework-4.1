def move_zeros_to_end(lst):

    non_zero_elements = [num for num in lst if num != 0]


    zero_count = lst.count(0)


    non_zero_elements.extend([0] * zero_count)

    return non_zero_elements



my_list = [0, 1, 0, 3, 12]
result = move_zeros_to_end(my_list)
print(result)
