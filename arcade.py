import sys
import random
from enum import Enum
import argparse

parse = argparse.ArgumentParser(
    description='Play a cool game'
)
parse.add_argument(
    '-n', '--name', metavar='name',
    required=True, help='Name of the user'
)
args = parse.parse_args()


def arcade(name):
    game_count = 0
    games_won = 0

    def rps(name):
        nonlocal game_count
        nonlocal games_won
        com_num = random.choice(['1', '2', '3'])
        print(f'Hey, {name} \n pick an option from 1 for rock, 2 for paper or 3 for scissors....')
        player_num = input('What option do you want to pick? ')
        if player_num in ['1', '2', '3']:
            game_count += 1
            print(f'You chose the option {player_num} while the computer chose the option {com_num}')
            if (player_num == '1' and com_num == '3') or \
               (player_num == '2' and com_num == '1') or \
               (player_num == '3' and com_num == '2'):
                print(f'Congrats, {name}. You won!🎉🎉🎉')
                games_won += 1
            elif player_num == com_num:
                print('That\'s a tie!😲')
            else:
                print(f'Sorry, {name}. You lost!😢')
            print(f'Games count: {game_count}')
            print(f'Games won: {games_won}')
            win_percent = (games_won / game_count) if game_count > 0 else 0
            print(f'Win percentage: {win_percent:.2%}')
            other_turn()
        else:
            print(f'Invalid choice. Please choose 1, 2, or 3.')
            rps(name)

    def guess_number(name):
        nonlocal game_count
        nonlocal games_won
        guess_num = random.choice(['1', '2', '3'])
        print(f'Hey, {name}!')
        player_num = input(f'Guess a number from 1, 2 or 3: ')
        if player_num in ['1', '2', '3']:
            game_count += 1
            print(f'{name}, you chose {player_num} and the right number is {guess_num}!')
            if player_num == guess_num:
                games_won += 1
                print(f'{name}, you won!🎉🎉🎉')
            else:
                print(f'Sorry, {name}. You lost. Try harder next time.😢')
            print(f'Games count: {game_count}')
            print(f'Games won: {games_won}')
            win_percent = (games_won / game_count) if game_count > 0 else 0
            print(f'Win percentage: {win_percent:.2%}')
            other_turn()
        else:
            print(f'Invalid choice. Please choose 1, 2, or 3.')
            guess_number(name)

    def pick_game():
        game = input(f'Hey, {name}. What game do you want to play! \n 1- Rock Paper Scissors \n 2- Guess the Number: ')
        if game == '1':
            rps(name)
        elif game == '2':
            guess_number(name)
        else:
            print(f'Please, {name}. Pick a number from 1 or 2.')
            pick_game()

    def other_turn():
        choice = input('Do you want to play again? \nPress y for yes \nPress q for quit: ').lower()
        if choice == 'y':
            pick_game()
        elif choice == 'q':
            return
        else:
            print('Pick one of the available options (y or q).')
            other_turn()

    return pick_game


run = arcade(args.name)
run()
