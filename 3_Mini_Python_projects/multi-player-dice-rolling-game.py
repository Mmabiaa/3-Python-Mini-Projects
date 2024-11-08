import random

# Function to simulate rolling a dice
def roll():
    # Get the number of players
    while True:
        try:
            players = int(input('Enter the number of players (2-4): '))
            if players < 2 or players > 4:
                print("Please enter a valid number of players (2-4).")
            else:
                break
        except ValueError:
            print("Invalid input, please enter an integer between 2 and 4.")
    
    max_score = 50
    player_scores = [0] * players  # Initialize a list to store each player's score
    roll_options = ('y', 'n')

    while True:
        # Loop through each player's turn
        for player in range(players):
            print(f"\nPlayer {player + 1}'s turn")

            # Ask if the player wants to roll the dice
            roll_ = input('Would you like to roll (y/n): ').lower()
            if roll_ == 'n':
                print(f"Player {player + 1} has chosen to skip their turn.")
                continue  # Skip to the next player

            elif roll_ == 'y':
                roll_value = random.randint(1, 6)  # Roll the dice
                print(f"You rolled: {roll_value}")

                if roll_value == 1:
                    print("You rolled a 1! Your turn is over with 0 points added.")
                    player_scores[player] = 0  # Reset the player's score for this turn
                else:
                    player_scores[player] += roll_value  # Add roll to the player's total score

                print(f"Player {player + 1}'s current score: {player_scores[player]}")

                # Check if the player reached the target score
                if player_scores[player] >= max_score:
                    print(f"\nPlayer {player + 1} wins with {player_scores[player]} points!")
                    return  # End the game if a player wins
            else:
                print("Invalid input. Please enter 'y' to roll or 'n' to skip the turn.")

            # Display the updated scores after each player's turn
            print("\nCurrent scores:")
            for i in range(players):
                print(f"Player {i + 1}: {player_scores[i]} points")

def main():
    roll()

main()
