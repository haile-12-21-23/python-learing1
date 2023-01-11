numbers = (1, 2, 3)
print(numbers[0])
print(numbers)
# tuple cannot modify, it  is immutable
# unpacking working on lists and tuples
coordinate = (1, 2, 3)
x = coordinate[0]
y = coordinate[1]
z = coordinate[2]
print(x)
print(y)
print(z)
# the same as
x, y, z = coordinate
print(x)
print(y)
print(z)
