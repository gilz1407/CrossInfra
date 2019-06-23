import json

list = [[1, 2, (3, 4)],['a','b','c']] # Note that the 3rd element is a tuple (3, 4)
j=json.dumps(list) # '[1, 2, [3, 4]]'
print(type(j))
j=json.loads(j)
print(type(j))
print(j)