# list in python
names = ['Haile', 'Abebe', 'Alemu', 'John', 'Marry']
print(names)  # gives ['Haile', 'Abebe', 'Alemu', 'John', 'Marry']
print(names[3])  # gives John
print(names[3:])  # gives ['John', 'Marry']
print(names[-1])  # gives Marry
# challenges
# write a program  to define largest number in a list
numbersInList = [23, 45, 21, 56, 23, 67, 34, 90, 89, 100]
largest = numbersInList[0]
for i in numbersInList:
    if largest < i:
        largest = i
print(largest)
# 2D lists equivalent to matrix in maths
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][1])  # gives 2
for row in matrix:
    for item in row:
        print(item)
# list methods
number = [5, 6, 3, 2, 1]
number.insert(0, 67)
number.sort()
print(number)
number1 = number.copy()
print(number1)
number.remove(6)
print(number)
number.pop()

print(number)
number.clear()
print(number)
number.append(34)
print(number)
print(30 in number)
print(number.count(3))
# challenge
# Write a program to remove the duplicates in list
duplicateNumber = [56, 43, 2, 3, 2, 4, 3, 56, 43]
for item in duplicateNumber:
    if duplicateNumber.count(item) > 1:
        duplicateNumber.remove(item)
print(duplicateNumber)
# or in the other methods
unique = []
for i in duplicateNumber:
    if i not in unique:
        unique.append(i)
print(unique)
