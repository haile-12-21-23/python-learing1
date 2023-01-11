command = ''
started = False
while True:
    command = input('>').lower()
    if command == 'start':
        if started:
            print('Car is already started!')
        else:
            started = True
            print('Car started...')
    elif command == 'stop':
        if not started:
            print('Car is already stooped!')
        else:
            started = False
            print('Car Stopped.')
    elif command == 'help':
        print('''
start - to start the car
stop - to stop car
quit - to quit game
        ''')
    elif command == 'quit':
        break
    else:
        print('Sorry I don\'t understand that! please type \'help \'')
