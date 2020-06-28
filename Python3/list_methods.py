lis = list()
lis.append('a')
lis.extend('abc')
lis.extend((2, 4, 4))
lis.extend({'one': 1, 'two': 2})
lis.extend({'one': 1, 'two': 2}.values())
lis.remove('a')
# Cannot remove muultiple elements as you know the data structure
# print(lis)
# print([int(item) for item in lis if isinstance(item, int)].sort())  # Returns None
# print(lis)  # Hence this list does not change

lis2 = [4, 6, 8, 9, 5, 7, 2, 4]
lis3 = [4, 6, 8, 9, 5, 7, 2, 4]
lis2.sort()  # Sorts in place
lis3_sorted = sorted(lis3)  # Does not change the original list
print(lis3, lis3_sorted)
