list1 = [1, 2, 3]
list2 = [4, 5, 6]
map_list = map(lambda x, y: x + y, list1, list2)
print(list(map_list))