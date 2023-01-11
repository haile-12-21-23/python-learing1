# dictionary
customer = {
    'name': 'Haile Addisu',
    'age': 25,
    'isVerified': True
}
name = customer['name']
age = customer['age']
print(name)
print(age)
# update data
customer['name'] = "Abebe"
print(customer['name'])
# adding key value
customer['birthDate'] = 'Dec 30 1997'
# get method
print(customer.get('birthDate'))
# challenges
# phone :1234 output should be One Two Three Four

phone = input('Phone: ')
digitMapping = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
}
output = ''
for ch in phone:
    output += digitMapping.get(ch, '!')+' '
print(output)
# emoji output
message = input('>')
words = message.split(' ')
emojis = {
    ':)': '😀',
    ':(': '😔'

}
output = ''
for word in words:
    output += emojis.get(word, word)+' '
print(output)
