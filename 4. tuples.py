print('all hail the tuples')

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
    print(dimension)

#you cannot change tuple, as you can change a list

# dimensions[0]=('audi')
# print(dimensions)
# dimensions[0]=300
# print(dimensions)

# dimensions.append('audi')
# print(dimensions)

#this would make a tuple and give an output of (3,)
tuple1=(3,)
print(tuple1)

#Writing over a Tuple, this works because reassigning variable is fine

print("original tuple")
dimension=(100,30)
for d in dimension:
    print(d)

print("modified tuple")
dimension=("audi","bmw")
for e in dimension:
    print(e)

