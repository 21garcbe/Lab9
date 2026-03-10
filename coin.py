"""
Coin.py
Author: Ben Garcia
A simple coin class for representing a coin 
with a heads/tails attribute and a method to flip the coin.
contains a constructor that initalizes the coin, a method called toss() that simulates tossing the coin,
a method called get_sideup() that return the current state of the coin
"""

import random
class Coin:
    """
    A class representing a coin that can be tossed.
    The coin keeps track of whether it is currently Heads or Tails.
    """

    def __init__(self):
        """Initializes the coin with a random side up."""
        if random.randint(0, 1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def toss(self):
        """Simulates tossing the coin by randomly setting it to Heads or Tails."""
        if random.randint(0, 1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):
        """Returns the current side of the coin."""
        return self.__sideup