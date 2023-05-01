#!/usr/bin/python3
"""RZFeeser | Alta3 Research
Creating a simple dice program utilizing classes."""


# imports from cheadice.py (this is in the local directory)
from cheatdice import Player
from cheatdice import Cheat_Swapper
from cheatdice import Cheat_Loaded_Dice
from cheatdice import Cheat_ldd_Dice

def main():
    """run-time code"""

    # create two cheater objects
    cheater1 = Cheat_ldd_Dice() # ability is to change 3rd dice roll to 6
    cheater2 = Cheat_Loaded_Dice() # increase all rolls by +1 provided they are < 6

    ch1Score = 0
    ch2Score = 0
    myRange = int(input("Number of games:\n>"))

    for i in range(myRange):

        # both players take turns
        cheater1.roll()
        cheater2.roll()

        # both players use their cheat methods
        cheater1.cheat()
        cheater2.cheat()

        print(f"Cheater 1 rolled {cheater1.get_dice()}")
        print(f"Cheater 2 rolled {cheater2.get_dice()}")

        if sum(cheater1.get_dice()) == sum(cheater2.get_dice()):
            print("Draw!")

        elif sum(cheater1.get_dice()) > sum(cheater2.get_dice()):
            print("Cheater 1 wins!")
            ch1Score += 1

        else:
            print("Cheater 2 wins!")
            ch2Score += 1

    print(f"After {myRange} rounds, the results are:\nCheater 1: {ch1Score}\nCheater 2: {ch2Score}")

if __name__ == "__main__":
    main()

