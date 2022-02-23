# python array can mix types
array = [10,3,"Adam",5]
print(array)

# random indexing -- indices start with 0
print(array[0])

# get all items
print(array[:])

# get first 3 items
print(array[:3])

# get item at index 1 and 2
print(array[1:3])

# get all items except for last one
print(array[:-1])

# get all items except last two
print(array[:-2])

# update
array[2] = 4
print(array[:])

# find maximum item (linear search; O(N))
max_item = array[0]
for num in array:
    if num > max_item:
        max_item = num

print(max_item)
