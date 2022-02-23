d = {'name':'Kevin', 'age':34, 'gender':'male'}

print(d['name']) # Kevin
print(d.keys())
print(d.values())

for key, value in d.items():
	print(value)

d.clear()
print(d.items())

del d # d no longer exists