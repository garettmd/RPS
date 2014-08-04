__author__ = 'Garett Dunn'
from random import randint


class Game:

    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.cheats = 0
        self.games = 0
        self.played = 0


    def whowins(self, compare1, compare2):
        self.played -= 1
        if compare1 == compare2:
            self.ties += 1
            print("You tied")
        elif (compare1 - compare2) % 3 == 1:
            self.wins += 1
            print("You won!")
        else:
            self.losses += 1
            print("You lost...")


def main():
    game = Game()
    try:
        game.games = int(input("How many games of RPS would you like to play?"))
    except ValueError:
        print("Please enter a number")
    else:
        computer = randint(0, 2)
        choice = input("Choose your weapon - (R)ock, (P)aper, or (S)cissors").lower()

        while game.played > 0:
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
                game.cheats += 1
        print("You won {0} games, lost {1}, and tied for {2}.".format(game.wins,game.losses,game.ties))
        if game.cheats > 0:
            print("You also cheated {0} times, you cheater.".format(cheats))

main()