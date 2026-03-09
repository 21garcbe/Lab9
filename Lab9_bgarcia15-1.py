"""

Main game logic for coin game (Lab9)
Author: Ben Garcia

Creates objects of coin and player classes
and simulates a coin flipping game where players take turns flipping a coin

"""
from player import Player

def main():
    """Main function to run the coin flipping game."""
    # Create two player objects
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    rounds = 75
    for i in range(rounds):
        print(f"Round {i + 1}:")
        
        # Player 1's turn
        player1.toss_coin()
        print(f"{player1.get_name()} tosses the coin and gets {player1.get_coin_sideup()}")
        if player1.get_coin_sideup() == "Heads":
            player1.add_coin()
        
        # Player 2's turn
        player2.toss_coin()
        print(f"{player2.get_name()} tosses the coin and gets {player2.get_coin_sideup()}")
        if player2.get_coin_sideup() == "Heads":
            player2.add_coin()
        
        print()  # Print a blank line

main()