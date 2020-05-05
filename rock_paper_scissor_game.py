from random import randint
# rock will beat scissors
# paper will beat rock
# scissors will beat paper
print('rock...')
print('paper...')
print('scissors...')
player_score = 0
computer_score = 0
no_of_win = 3
rand_num = randint(1, 3)
if rand_num == 1:
    computer = 'rock'
elif rand_num == 2:
    computer = 'paper'
else:
    computer = 'scissors'

while player_score < no_of_win and computer_score < no_of_win:
    play_game = input("Do you want to play? y/n: ")
    if play_game == 'n':
        break

    else:
        print(f'Player Score={player_score}')
        print(f'Computer Score={computer_score}')

        player = input('Player choose, rock, paper or scissors: ').lower()
        print(f'The computer said {computer}')

        if player == computer:
            print('It\'s a tie!')

        elif player == 'rock' or player == 'paper' or player == 'scissors':
            if player == 'rock' and computer == 'scissors':
                player_score += 1
                print('player wins!')

            elif player == 'paper' and computer == 'rock':
                print('player wins!')
                player_score += 1

            elif player == 'scissors' and computer == 'paper':
                print('player wins!')
                player_score += 1
            else:
                print('computer wins!')
                computer_score += 1
print(f'Player score={player_score} and Computer score={computer_score}')
