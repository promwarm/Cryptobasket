import Insert_coins as ic

def show_menu():
    print('1. Show portfolio')
    print('2. Add / remove coins')
    print('3. Refresh exchange rates of coins in your portfolio')
    print('')
    print('9. Exit')

def handle_input():
    try:
        MyChoice = int(input('What would you like to do? '))
        if MyChoice == 1:
            print('Function not available')
        elif MyChoice == 2:
            coin = ic.ask_coins()
            print(ic.parse_coin(coin)) # output is a json for now
        elif MyChoice == 3:
            print('Function not available')
        elif MyChoice == 9:
            quit()
        else:
            handle_input() # Please make a valid choice
    except Exception as err:
        #handle_input() # Instead of showing an error, just try again
        print ('Incorrect input: ' +str(err))

show_menu()
handle_input()