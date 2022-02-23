array = [10, 3, 7, 5]

# random indexing: indexes start with 0
# get all items
a1 = array[:]
# get first 3 items
a2 = array[0:2]
# get all items except last one
a3 = array[:-1]
# get all items except last two
a4 = array[:-2]

# in python we can mix types
array2 = [10.0, 3, 'Adam', 5]

# updating
array[2] = 'Kevin'

# linear search O(N)
def getmax(array):
	max = array[0]
	for num in array:
		if num > max:
			max = num
	print(max)

