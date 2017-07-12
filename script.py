from random import random


class Game:
    rand = 0
    guessed = False
    number_guessed = 0

    def run_game(self):

        self.rand = random() * 100
        self.rand = round(self.rand, 0)
        print("Guess the number [1 - 100]")
        self.get_input()

    def get_input(self):

        answer = input()

        if answer.isdigit():
            self.number_guessed = int(answer)
            self.check_numbers()
        else:
            print("Please enter a number")
            self.get_input()

    def check_numbers(self):

        n = int(self.number_guessed)

        while not self.guessed:
            if n > self.rand:
                print("Number is less than " + str(n))
                self.get_input()
            elif n < self.rand:
                print("Number is greater than " + str(n))
                self.get_input()
            else:
                print("You have guessed the correct number!")
                self.guessed = True
                return self.guessed


if __name__ == "__main__":
    game = Game()
    game.run_game()
