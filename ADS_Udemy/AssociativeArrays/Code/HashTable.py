class HashTable:
	def __init__(self):
		# based on the load factor we may change the size of the underlying DS (dynamic resizing)
		self.capacity = 10
		self.keys = [None]*self.capacity
		self.values = [None]*self.capacity

	# hash value (index of the array) based on the key
	def hash_function(self, key):
		hash_sum = 0
		# ord transforms character into ASCII value
		for letter in key:
			hash_sum += ord(letter)

		return hash_sum % self.capacity

	def insert(self, key, data):
		# we have to find a valid location for the value(data)
		index = self.hash_function(key)

		# there may be collisions which means that the index is already occupied
		# while we do not find an empty array slot
		while self.keys[index] is not None:
			# sometimes we have to update the value if the key is already present
			if self.keys[index] == key:
				self.values[index] = data
				return

			# do linear probing (try next slot in the array)
			# because we may increment the index such that we are outside the range of the underlying list DS
			index = (index+1) % self.capacity

		# we have found the valid slot for the item so we have to insert the data
		self.keys[index] = key
		self.values[index] = data

	def get(self, key):
		# we have to find a valid location for the value (data)
		index = self.hash_function(key)

		while self.keys[index] is not None:
			# this is when we find the item we are looking for
			if self.keys[index] == key:
				return self.values[index]
			index = (index+1) % self.capacity

		# the given key value pair with key does not exist in the hashtable
		return None

if __name__ == '__main__':
	table = HashTable()
	table.insert('Adam', 23)
	table.insert('Kevin', 45)
	table.insert('Daniel', 34)
	table.insert('Daniel', 33) #value is updated to 33
	print(table.get('Ana')) # none
	print(table.get('Adam')) # 23
	print(table.get('Kevin')) # 45
	print(table.get('Daniel')) # 33
