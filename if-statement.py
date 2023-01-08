isHot = False
isCold = False
if isHot:
    print('It\'s a hot day')
    print('Drink plenty of water')
elif isCold:
    print('It\'s a cold day')
    print('Wear warm clothes')
else:
    print('It\'s a lovely day')

print('Enjoy your day')
# exercise
price = 1000000
hasGoodCredit = True
if hasGoodCredit:
    downPayment = 0.1*price
else:
    downPayment = 0.2*price
print(f'Down payment: ${downPayment}')
# logical operators AND OR NOT
hasHighIncome = True
hasGoodCredit = True
hasCriminalRecord = False
if hasHighIncome and hasGoodCredit:
    print('Eligible for loan')
if hasGoodCredit and not hasCriminalRecord:
    print('Eligible for loan')
