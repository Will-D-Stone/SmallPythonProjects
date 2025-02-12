from random import choice 
import time

#Variable creation: moves list, playAgain set to "Y" to start while loop in game logic, Scores set at 0 to incrememnt in scoring
moves = {'rock' : 'r', 'paper': 'p', 'scissors': 's'}
playAgain = "Y" #initialize this to "Y" to start the while loop
computerScore = 0
playerScore = 0

#While loop to allow for multiple rounds before game end
while playAgain == "Y":

    #Player input, spell check, case check
    player = input('rock, paper, or scissors? ').lower()
    while player != 'rock' and player != 'paper' and player != 'scissors' and player != 'exit':
        print("Error: unknown response")
        player = input("Please input 'rock', 'paper', 'scissors', or 'exit' to end: ")

    if player == 'exit':
        print("Thanks for playing!")
        break

    #Computer decision and depiction of both choices
    computer = choice(list(moves.keys()))

    print(f"\nYou: {moves[player]}")
    time.sleep(0.5)
    print(f"Computer: {moves[computer]}")
    time.sleep(0.5)

    #Game logic and scoring

    if player == computer:
        print("Tie!")

    elif (player == 'rock' and computer == 'scissors') or\
        (player == 'paper' and computer == 'rock') or\
        (player == 'scissors' and computer == 'paper'):
        print("You Win")
        playerScore = playerScore + 1

    else:
        print("Computer Wins")
        computerScore = computerScore + 1
    
    #Score display and continuation check
    print(f"\nPlayer: {playerScore} - Computer: {computerScore}")
    temp = input("Did you want to play again? Y/N: ").upper()
    
    while temp != "Y" and temp != "N":
        print("Error: unknown response")
        temp = input("Did you want to play again? Y/N: ").upper()
    playAgain = temp
if computerScore > playerScore:
    print("Computer Wins!")
elif playerScore > computerScore:
    print("You Win!")
elif computerScore == playerScore:
    print("It's a tie")
else:
    print("Something went wrong with the scoreboard")

print("Thanks for playing!")