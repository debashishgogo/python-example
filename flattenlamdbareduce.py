from functools import reduce
my_list = [[1], [2, 3], [4, 5, 6, 7]]
print(reduce(lambda x, y: x + y, my_list))
