from random import random


class Game:

    # This function handles the number guessing and number formatting
    def run_game(self):

        # rand is declared by grabbing a number between 0 and 1, multiplying it by 100, and rounds to nearest integer
        rand = round(random() * 100, 0)
        print("Guess the number [0 - 100]")
        guesses = 0

        while True:

            # Assigns the 'answer' variable by grabbing user input from console
            answer = input()

            # Checks if the input from the console is a number, and if not, asks the user to enter a valid number
            if answer.isdigit():
                n = int(answer)
                if n > int(rand):
                    print("Number is less than " + str(n))
                    guesses = guesses + 1
                elif n < int(rand):
                    print("Number is greater than " + str(n))
                    guesses = guesses + 1
                else:
                    guesses = guesses + 1
                    print("It took you " + str(guesses) + " guesses to guess the right number!")
                    reply = self.play_again()
                    if reply is False:
                        break
                    else:
                        self.run_game()
            else:
                print("Please enter a number")

    @staticmethod
    def play_again():

        while True:
            reply = input("Play again? (y/n)")
            if reply.lower() == "y":
                return True
            elif reply.lower() == "n":
                return False
            else:
                print("Enter 'y' or 'n'")


if __name__ == "__main__":
    game = Game()
    game.run_game()
