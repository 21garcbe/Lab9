"""
player.py
Author: Ben Garcia
A simple player class for representing a player in a coin flipping game.
The player has a name and 'wallet' of coins, and a coin object to flip.
"""
from coin import coin
class Player:
    """A class representing a player object with a name, wallet of coins, and a coin object to flip."""
    
    def __init__(self, name):
        """Constructor that initializes the player's name, wallet of coins, and a coin object to flip."""
        self.__name = name
        self.__wallet = 0
        self.__coin = coin()

    def get_name(self):
        """Returns the player's name."""
        return self.__name

    def get_wallet(self):
        """Returns the player's wallet of coins."""
        return self.__wallet

    def add_coin(self):
        """Adds a coin to the player's wallet."""
        self.__wallet += 1

    def lose_coin(self):
        """removes a coin from the player's wallet."""
        if self.__wallet > 0:
            self.__wallet -= 1

    def toss_coin(self):
        """Flips the player's coin and returns the result."""
        self.__coin.toss()
      
    def get_coin_sideup(self):
        """Returns the current state of the player's coin."""
        return self.__coin.get_sideup()