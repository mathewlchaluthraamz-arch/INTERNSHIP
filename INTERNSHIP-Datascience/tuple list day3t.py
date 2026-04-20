
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print("Original tuple:", my_tuple)


temp_list = list(my_tuple)

temp_list[2] = 99


my_tuple = tuple(temp_list)

print("Updated tuple:", my_tuple)