__author__ = 'Garett Dunn'
from random import randint


class Game:
    wins = 0
    losses = 0
    ties = 0
    cheats = 0
    games = 0
    played = 0
    finished = ""

    def __init__(self):
        pass

    def whowins(self, compare1, compare2):
        Game.games += 1
        if compare1 == compare2:
            Game.ties += 1
            Game.played += 1
            print("You tied")
        elif (compare1 - compare2) % 3 == 1:
            Game.wins += 1
            Game.played += 1
            print("You won!")
        else:
            Game.losses += 1
            Game.played += 1
            print("You lost...")
        if Game.games == Game.played:
            Game.finished = "yes"


def main():
    try:
        Game.games = int(input("How many games of RPS would you like to play?"))
    except ValueError:
        print("Please enter a number")
    else:
        while Game.played <= Game.games:
            computer = randint(0, 2)
            choice = input("Choose your weapon - (R)ock, (P)aper, or (S)cissors").lower()
            game = Game()
            if choice == "r":
                player = 0
                game.whowins(player, computer)
            elif choice == "p":
                player = 1
                game.whowins(player, computer)
            elif choice == "s":
                player = 2
                game.whowins(player, computer)
            else:
                print("You have only have three choices, stop trying to make up other weapons.")
                Game.cheats += 1
        print("You won {0} games, lost {1}, and tied for {2}.".format(wins,losses,ties))
        if Game.cheats > 0:
            print("You also cheated {0} times, you cheater.".format(cheats))

main()