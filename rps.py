

# Barebones RPS function to be used with other classes/objects for functionality
# Returns 1 if Player 1 won, 2 if Player 2 won, and 3 for a draw (both picked same)
# Feel free to add more functionality as the site becomes more complex

def rps(player1, player2):
    if player1 == player2:
        print("It's a tie")
        return 3 # Tie, run again
    elif player1 == "rock" and player2 == "scissors":
        print("Player 1 Wins")
        return 1 # Player 1 wins
    elif player1 == "scissors" and player2 == "paper":
        print("Player 1 Wins")
        return 1 # Player 1 wins
    elif player1 == "paper" and player2 == "rock":
        print("Player 1 Wins")
        return 1 # Player 1 wins
    elif player2 == "rock" and player1 == "scissors":
        print("Player 2 Wins")
        return 2
    elif player2 == "scissors" and player1 == "paper":
        print("Player 2 Wins")
        return 2
    elif player2 == "paper" and player1 == "rock":
        print("Player 2 Wins")
        return 2
    else: 
        print("Error: Incompatible inputs received")
        return 0
