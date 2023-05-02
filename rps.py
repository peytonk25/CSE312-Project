

# Barebones RPS function to be used with other classes/objects for functionality
# Returns 1 if Player 1 won, 2 if Player 2 won, and 3 for a draw (both picked same)
# Feel free to add more functionality as the site becomes more complex

def rps(player1, player2):
    if player1 == player2:
        return 3 # Tie, run again
    elif player1 == "rock" and player2 == "scissors":
        return 1 # Player 1 wins
    elif player1 == "scissors" and player2 == "paper":
        return 1 # Player 1 wins
    elif player1 == "paper" and player2 == "rock":
        return 1 # Player 1 wins
    elif player1 == "rock" and player2 == "scissors":
        return 2
    elif player1 == "scissors" and player2 == "paper":
        return 2
    elif player1 == "paper" and player2 == "rock":
        return 2
    else: 
        print("Error: Incompatible inputs received")
        return 0
