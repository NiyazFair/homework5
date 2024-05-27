immutable_var = ([1, 2], 3, 5, 'string')
print(immutable_var)
immutable_var[0][0] = 3
print(immutable_var)
mutable_list = [1, 2, 3, 4, 5, 'a', 'b']
mutable_list[0] = 7
print(mutable_list)
mutable_list[3] = 9
print(mutable_list)
mutable_list[5] = 11
print(mutable_list)