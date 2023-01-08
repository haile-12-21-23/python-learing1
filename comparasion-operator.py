temperature = 30

if temperature > 30:
    print('It\'s a hot day')

elif temperature < 10:
    print('It\'s a cold day')
else:
    print('It\'s neither a hot nor a cold day')
name = 'Haile'
length = len(name)
if length < 3:
    print('Name must be at least 3 characters.')
elif length > 50:
    print('Name must be a maximum of 50 characters.')
else:
    print('Name looks good!')
weight = input('What is your weight? ')
unit = input('L(for pounds) or K(for kilograms? ')
if unit.upper() == 'L':
    print('your are ', int(weight)//0.45, 'pounds')
elif unit.upper() == 'K':
    print('You are', int(weight)*0.45, 'kilo grams')
