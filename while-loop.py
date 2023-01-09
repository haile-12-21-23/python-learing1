guessLimit = 1
j = 1
while guessLimit <= 5:

    while j <= guessLimit:
        print('*'*guessLimit)
        j += 1
    guessLimit += 1
print('Done')
# Guess game
secretNumber = 9
guessLimit = 3
guessCount = 0
while guessCount < guessLimit:
    guess = int(input('Guess:'))
    guessCount += 1

    if guess == secretNumber:
        print('You win!')
        break
else:
    print('Sorry,You failed')
