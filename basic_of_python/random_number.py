import random


members = ['John', 'Mary', 'Bob', 'Mosh']
for i in range(3):
    print(random.randint(10, 20))
selected = random.choice(members)
print(selected)
# Dice


class Dice:
    def roll(self):
        piked = random.randint(1, 6)
        return piked


dice = Dice()
result = dice.roll()
print(result)
