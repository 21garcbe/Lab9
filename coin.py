"""
Coin.py
Author: Ben Garcia
A simple coin class for representing a coin 
with a heads/tails attribute and a method to flip the coin.
contains a constructor that initalizes the coin, a method called toss() that simulates tossing the coin,
a method called get_sideup() that return the current state of the coin
"""

import random
class coin:
    """A class representing a coin with a heads/tails attribute and a method to flip the coin."""

    def __init__(self):
        """Constructor that initializes the coin to heads."""
        self.__sideup = ""

    def toss(self):
        """Simulates tossing the coin by randomly setting the sideup attribute to either heads or tails."""
        if random.randint(0, 1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):
        """Returns the current state of the coin."""
        return self.__sideup
