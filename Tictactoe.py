from colorama import Back
import random

obj = ['Hammer', 'Scrissor', 'Paper']
history = []

def ply_input():
    while True:
        ply_input = int(input("Please select these choices\n\n1. Hammer\n\n2. Scrissor\n\n3. Papers\n\n>>> "))
        if not None or ply_input >= 1 or ply_input <= 3:
            return obj[ply_input-1]

while True:
    ply_turn = ply_input()
    print('Player Choose : ', ply_turn)
    com_turn = random.choice(obj)
    print('Computer choose : ', com_turn)

    if ply_turn == 'Hammer':
        if com_turn == 'Hammer':
            print(Back.YELLOW, 'Draw!', Back.RESET)
            history.append('=')
        elif com_turn == 'Scrissor':
            print(Back.GREEN, 'Gain!', Back.RESET)
            history.append('O')
        elif com_turn == 'Paper':
            print(Back.RED, 'Lost!', Back.RESET)
            history.append('X')

    elif ply_turn == 'Scrissor':
        if com_turn == 'Hammer':
            print(Back.RED, 'Lost!', Back.RESET)
            history.append('X')
        elif com_turn == 'Scrissor':
            print(Back.YELLOW, 'Draw!', Back.RESET)
            history.append('=')
        elif com_turn == 'Paper':
            print(Back.GREEN, 'Gain!', Back.RESET)
            history.append('O')

    elif ply_turn == 'Paper':
        if com_turn == 'Hammer':
            print(Back.GREEN, 'Gain!', Back.RESET)
            history.append('O')
        elif com_turn == 'Scrissor':
            print(Back.RED, 'Lost!', Back.RESET)
            history.append('X')
        elif com_turn == 'Paper':
            print(Back.YELLOW, 'Draw!', Back.RESET)
            history.append('=')

    if history.count('X') + history.count('O') == 3:
        if history.count('X') < history.count('O'):
            print(Back.GREEN, '\t\tYou Win!\t\t', Back.RESET)
            break
        else:
            print(Back.RED, '\t\tYou Lost!\t\t', Back.RESET)
            break