def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        letter = input('Are you choosing X or O? >').upper()

    if letter == 'X':
        return ['X', 'O'] #player, bot
    else:
        return ['O', 'X'] #player, bot

# print(inputPlayerLetter()) #check!

def choiceX():
    pass

def printWelcome():
    menu = '''
    Menu:
    1. Choice X
    2. Choice O
    3. Random
    4. Input
    '''
    print(menu)
    choice = 0
    while not (choice == 1 or choice == 2 or choice == 3 or choice == 4):
        choice = int(input('Are you choosing 1 or 2 or 3 or 4? >')) # str -> int

    if (choice == 1):
        return choiceX()



print(printWelcome())