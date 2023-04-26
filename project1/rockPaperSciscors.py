#!/usr/bin/env python3

# This is a classic rock paper scissors game via text
# You will play against the computer which will choose randomly
import random


def main():
    rounds = None
    while rounds is None:
        try:
            rounds = int(input("How many rounds do you want to play?"))
        except ValueError:
            print("Invalid Number!")
        if rounds and rounds < 1:
            print("Invalid Number!")
            rounds = None
        elif rounds and rounds > 9:
            print("Too many rounds!")
            rounds = None

    print(f"You will play against the computer for {rounds} rounds.")

    options = {
            1:"rock",
            2:"paper",
            3:"scissors"
            }
    round = 0
    userScore = 0
    cpuScore = 0
    while round < rounds:
        round += 1
        userChoice = None
        while userChoice is None:
            for i in range(len(list(options.keys()))):
                print(f"{list(options.keys())[i]}: {list(options.values())[i]}")
            userChoice = input("Pick your move!\n> ").lower()
            try:
                userChoice = int(userChoice)
            except ValueError:
                if userChoice == "rock":
                    userChoice = 1
                elif userChoice == "paper":
                    userChoice = 2
                elif userChoice == "scissors":
                    userChoice = 3
                else:
                    userChoice = None
                    print("Invalid Choice!")
            if userChoice and (userChoice < 1 or userChoice > 3):
                print("Invalid Choice!")
                userChoice = None
            elif not userChoice:
                print("Invalid Choice!")
        print(f"You picked {options[userChoice]}.")
        cpuChoice = random.randint(1, 3)
        print(f"The computer picked {options[cpuChoice]}.")

        if userChoice == cpuChoice:
            print(f"Round {round} is a tie!")
        elif (userChoice == 1 and cpuChoice == 2) or (userChoice == 2 and cpuChoice == 3) or (userChoice == 3 and cpuChoice == 1):
            print(f"You lost round {round}!")
            cpuScore += 1
        else:
            print(f"You won round {round}!")
            userScore += 1
        print(f"Current Scores:\nPlayer: {userScore} || CPU: {cpuScore}")
    
    print(f"End of Game!\nFinal Scores:\nPlayer: {userScore} || CPU: {cpuScore}")
    if userScore > cpuScore:
        print("You won!")
    elif userScore < cpuScore:
        print("You lost.")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
