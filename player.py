"""
player.py
Author: Ben Garcia
A simple player class for representing a player in a coin flipping game.
The player has a name and 'wallet' of coins, and a coin object to flip.
"""
from coin import Coin

class Player:
    """
    Represents a player in the Match Coins game.
    Each player has a name, a wallet of coins, and a Coin object they can toss.
    """

    def __init__(self, name):
        """
        Initializes the player with a name, a wallet of 20 coins,
        and creates a Coin object.
        """
        self.__name = name
        self.__wallet = 20
        self.__coin = Coin()

    def toss_coin(self):
        """Tells the player's coin to toss itself."""
        self.__coin.toss()

    def get_coin_side(self):
        """Returns the current side of the player's coin."""
        return self.__coin.get_sideup()

    def win_coin(self):
        """Adds one coin to the player's wallet."""
        self.__wallet += 1

    def lose_coin(self):
        """Subtracts one coin from the player's wallet."""
        self.__wallet -= 1

    def get_wallet(self):
        """Returns the number of coins in the player's wallet."""
        return self.__wallet

    def get_name(self):
        """Returns the player's name."""
        return self.__name