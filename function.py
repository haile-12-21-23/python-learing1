def greetingUser(firstName, lastName):
    print(f'Hi {firstName} {lastName}')
    print('Welcome abroad')


print('Start')
# positional arguments
greetingUser("Haile", 'Addisu')
# keyword arguments
# we can use keyword argument after positional argument
# but we cannot use keyword arguments before positional arguments
greetingUser(lastName="Marry", firstName='John')
print('finish')
# return value from function


def square(number):
    return (number*number)


result = square(3)
print(result)
# NB: all python functions by default return None.


def emojisConvertor(message):
    words = message.split(' ')
    emojis = {
        ':)': '😀',
        ':(': '😔'

    }
    output = ''
    for word in words:
        output += emojis.get(word, word)+' '
    return output


message = input('>')
response = emojisConvertor(message=message)
print(response)
