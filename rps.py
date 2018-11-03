# rps.py
import random

def get_human_input(input=input):
    human = input('rock, paper or scissors? ')
    while not is_valid_input(human):
        human = input('rock, paper or scissors? ')
    return human

def is_valid_input(human_input):
    return human_input in ['rock', 'paper', 'scissors']

def generate_computer_play():
    return random.choice(['rock', 'paper', 'scissors'])

def evaluate(human, computer):
    if human == computer:
        return('tie')
    elif human == 'rock':
        if computer == 'paper':
            return('computer')
        else:
            return('human')
    elif human == 'paper':
        if computer == 'scissors':
            return('computer')
        else:
            return('human')
    elif human == 'scissors':
        if computer == 'rock':
            return('computer')
        else:
            return('human')

def main(input=input):
    human = get_human_input(input)
    computer = generate_computer_play()
    print(computer)
    game = evaluate(human, computer)
    if game == 'tie':
        print('It\'s a tie')
    else:
        print(f'{game} won')

if __name__ == '__main__':
    main()
