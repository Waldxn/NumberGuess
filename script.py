from random import random


class Game:
    rand = round(random() * 100, 0)
    guessed = False
    number_guessed = 0
    print("Guess the number [1 - 100]")

    def run_game(self):

        answer = input()

        if answer.isdigit():
            self.number_guessed = int(answer)
            n = int(self.number_guessed)

            while not self.guessed:
                if n > int(self.rand):
                    print("Number is less than " + str(n))
                    self.run_game()
                elif n < int(self.rand):
                    print("Number is greater than " + str(n))
                    self.run_game()
                else:
                    print("You have guessed the correct number!")
                    self.guessed = True
                    return self.guessed
        else:
            print("Please enter a number")
            self.run_game()
            return

if __name__ == "__main__":
    game = Game()
    game.run_game()
