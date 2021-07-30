import random

def play():
    user = input("\nWant to play a game? Enter 'rock', 'paper' or 'scissors': ").lower()
    computer = random.choice(['rock', 'paper', 'scissors'])
    #user enters their choice,  then the computer enters a random choice

    if user == computer:
        return 'Game result: it\'s a tie!', computer
    #if the user and the computer have the same input, it's a tie
    
    if user_win(user, computer):
        return 'Game result: you won!', computer
    
    return 'Game result: you lost!', computer

def user_win(player, opponent):
     if (player == 'rock' and opponent =='scissors') or (player == 'scissors' and opponent == 'paper') or (player == 'paper' and opponent == 'rock'):
         return True
    #returns True if user wins
    #rock beats scissors, scissors beat paper, paper beats rock

result, computer = play()

def main():
    while True:
        print('\nThe computer randomly entered "{}".'.format(computer))
        print(result)
        
        restart = input('\nWould you like to play again? If so, enter yes. ').lower()
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
