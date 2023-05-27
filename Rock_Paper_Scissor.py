import random
import math

def play():
    user = input("What's your choice? \n Rock 'r', Paper 'p', or Scissor 's' :")
    user = user.lower()

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return (0, user, computer)

    if is_win(user, computer):
        return (1, user, computer)

    return (-1, user, computer)

def is_win(player, opponent):
    # Return true if the player beats the opponent
    # Winning condition: r > s, s > p, p > r
    
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    else:
        return False

def play_count(n):
    # For the number of rounds
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)
    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result, user, computer = play()
        if result == 0:
            print('It\'s a tie. You and computer both chose {}'.format(user))
        elif result == 1:
            player_wins == 1
            print('You won :) You chose {} and computer chose {}'.format(user, computer))
        else:
            computer_wins == -1
            print('You lost :( You chose {} and computer chose {}'.format(user, computer))
        print('\n')
    
    if player_wins > computer_wins:
        print('You have won the best of {} games'.format(n))
    else:
        print('Computer won the games.')




if __name__ == '__main__':
    play_count(3)