import random
import os

class Game:
    """
    A class for the game of Rock-Paper-Scissors.
    """

    def __init__(self):
        """
        Initializes the game with options, scores, high score, and game history.
        """
        self.options = ["rock", "paper", "scissors"]
        self.user_score = 0
        self.computer_score = 0
        self.high_score = 0
        self.game_history = []

    def play(self):
        """
        Function to play rock-paper-scissors game
        """
        print("\033[1mWelcome to the game of Rock-Paper-Scissors.\033[0m")
        while True:
            # clear the console screen
            os.system('clear')

            # display the menu
            print("\033[1mMenu:\033[0m")
            print("1. Play")
            print("2. Help")
            print("3. Quit")

            # get user input
            user_choice = input("\033[1mPlease enter your choice: \033[0m").lower().strip()

            # check if input is valid
            if user_choice == '1':
                user_choice = input("\033[1mChoose rock, paper, or scissors: \033[0m").lower().strip()
                if user_choice not in self.options:
                    print("\033[1mInvalid choice. Please choose rock, paper, or scissors.\033[0m")
                    continue

                # get computer choice
                computer_choice = random.choice(self.options)

                # keep track of game history
                self.game_history.append((user_choice, computer_choice))

                # determine winner and update score
                if user_choice == computer_choice:
                    print("\033[1mYou chose {} and the computer chose {}. It's a tie!\033[0m".format(user_choice, computer_choice))
                elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
                    print("\033[1mYou chose {} and the computer chose {}. You win!\033[0m".format(user_choice, computer_choice))
                    self.user_score += 1
                else:
                    print("\033[1mYou chose {} and the computer chose {}. You lose!\033[0m".format(user_choice, computer_choice))
                    self.computer_score += 1
                print("\033[1mScore: User {} - Computer {}\033[0m".format(self.user_score, self.computer_score))
                if self.user_score > self.high_score:
                    self.high_score = self.user_score
                print("\033[1mHigh Score: {}\033[0m".format(self.high_score))
                input("\033[1mPress enter to continue...\033[0m")
            elif user_choice == '2':
                print("\033[1mHelp:\033[0m")
                print("The objective of the game is to beat the computer by choosing rock, paper or scissors.")
                print("rock beats scissors, scissors beats paper and paper beats rock.")
                input("\033[1mPress enter to continue...\033[0m")
            elif user_choice == '3':
                print("\033[1mGame Over. Thanks for playing!\033[0m")
                break
            else:
                print("\033[1mInvalid choice. Please choose a valid option.\033[0m")
                input("\033[1mPress enter to continue...\033[0m")

if __name__ == "__main__":
    game = Game()
    game.play()
