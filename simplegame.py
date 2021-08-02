import random

def play():
    user = input("\n:::::::::::::::::::::::::\nLet's play a game! \nChoose your weapon: enter 'rock', 'paper', 'scissors' or 'well': ").lower()
    computer = random.choice(['rock', 'paper', 'scissors', 'well'])
    print('\n:::::::::::::::::::::::::\nThe computer randomly entered "{}".\n\n⚡⚡⚡⚡⚡⚡⚡⚡\n'.format(computer))
    return user, computer
    #user enters their choice,  then the computer enters a random choice

def user_win(player, opponent):
    if player == opponent:
        return 'Game result: it\'s a tie!\n:::::::::::::::::::::::::\n'
    elif (player == 'rock' and opponent =='scissors') or (player == 'scissors' and opponent == 'paper') or (player == 'paper' and (opponent == 'rock' or 'well')) or (player == 'well' and (opponent =='scissors' or 'rock')):
         return 'Game result: you won!\n:::::::::::::::::::::::::\n'
    elif player not in ['rock', 'paper', 'scissors', 'well']:
        return 'Oops, enter a correct word.'
    else:
        return 'Game result: you lost!\n:::::::::::::::::::::::::\n'

def script():
    player, opponent = play()
    
    print(user_win(player, opponent))
    restart = input("Would you like to try again? ")
    if restart == "yes" or restart == "y":
        return(script())
    if restart == "no" or restart == "n":
        return("Thank you for playing!")

script()
