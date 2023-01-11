# String in python
course = 'Python for \"Beginners\"'
print(course)
# the same out put
course = 'Python for "Beginners"'
# negative index in python that gives from end -
# positive  index 0 = negative index -1
print(course[-2])  # out put is s
print(course[0:6])  # gives Python
# copy in python
copy = course[:]  # it gives Python for "Beginners"
print(copy)
name = 'Haile'
print(name[1:-1])  # it gives ail
# formatting strings
firstName = 'Haile'
lastName = 'Addisu'
message = firstName + ' ['+lastName+'] is coder.'  # string concatenation
msg = f'{firstName} [{lastName}] is coder'  # string formatting
print(message)
print(msg)
# knowing length ot strings
course = 'Python for Beginners'
print(len(course))
# convert to upper case
print(course.upper())
# knowing the index
print(course.find('Beginners'))  # return -1 if the letter does not exist
# replacing strings
print(course.replace('Beginners', 'Absolute Beginners'))
# checking string in the sentence
print('Python' in course)
# NB:all functions are case sensitive

# printing multi line strings
email = ''' 
Hi John
Here is our first email to you.

thank you for supporting the team

your friend
'''
print(email)
