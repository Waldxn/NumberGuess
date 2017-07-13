from random import random


class Game:
    """
    rand is declared by grabbing a number between 0 and 1, multiplying it by 100, and rounding to the nearest integer
    guessed is declared as false in order to keep the while loop running until the number is guessed
    """
    rand = round(random() * 100, 0)
    guessed = False
    print("Guess the number [1 - 100]")

    # This function handles the number guessing and number formatting
    def run_game(self):

        # Assigns the 'answer' variable by grabbing user input from console
        answer = input()

        # Checks if the input from the console is a number, and if not, asks the user to enter a valid number
        if answer.isdigit():

            n = int(answer)

            # Checks the input given against the random number generated
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
