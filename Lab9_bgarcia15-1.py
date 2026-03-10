"""

Main game logic for coin game (Lab9)
Author: Ben Garcia

Creates objects of coin and player classes
and simulates a coin flipping game where players take turns flipping a coin

"""

from player import Player

def main():
    """Main function to run the coin flipping game."""
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    print("-------Welcome to the Coin Flipping Game!--------")
    print(f"\n{player1.get_name()} starts with {player1.get_wallet()} coins.")
    print(f"\n{player2.get_name()} starts with {player2.get_wallet()} coins.")
    play = input("\nDo you want to play the game? (y/n): ")

    while play.lower() == 'y':

        #game over check condition
        if player1.get_wallet() <= 0:
            print(f"\n{player1.get_name()} has no coins left. {player2.get_name()} wins!")
            break
        if player2.get_wallet() <= 0:
            print(f"\n{player2.get_name()} has no coins left. {player1.get_name()} wins!")
            break

        #toss coins
        player1.toss_coin()
        player2.toss_coin()

        #get results
        coin1_side = player1.get_coin_side()
        coin2_side = player2.get_coin_side()

        #display resuls
        print(f"\n{player1.get_name()} tosses: {coin1_side}")
        print(f"{player2.get_name()} tosses: {coin2_side}")

        if coin1_side == coin2_side:
            print("It's a match! player 1 wins a coin from player 2.")
            player1.add_coin()
            player2.remove_coin()
        else:
            print("No match. player 2 wins a coin from player 1.")
            player2.add_coin()
            player1.remove_coin()

        #show wallets
        print(f"\n{player1.get_name()} has {player1.get_wallet()} coins left.")
        print(f"{player2.get_name()} has {player2.get_wallet()} coins left.")

        play = input("\nDo you want to play again? (y/n): ")
    
    #print final results
    print("\n-------Game Over!--------")
    print(f"\n{player1.get_name()} finished with {player1.get_wallet()} coins.")
    print(f"{player2.get_name()} finished with {player2.get_wallet()} coins.")

    if player1.get_wallet() > player2.get_wallet():
        print(f"\n{player1.get_name()} wins the game!")
    elif player2.get_wallet() > player1.get_wallet():
        print(f"\n{player2.get_name()} wins the game!")
    else:
        print("\nIt's a tie!")

if __name__ == "__main__":
    main()



    

