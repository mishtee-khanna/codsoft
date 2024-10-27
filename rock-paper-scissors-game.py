from tkinter import *
from random import choice

class RockPaperScissors:  # Formation of class RockPaperScissors
    def __init__(self):
        self.root = Tk()
        self.root.title("Rock Paper Scissors")
        self.root.geometry("300x200")
        self.user_score = 0
        self.computer_score = 0

        self.user_score_label = Label(self.root, text="Your Score: 0", font=("Futura", 12))
        self.user_score_label.pack()

        self.computer_score_label = Label(self.root, text="Computer Score: 0", font=("Futura", 12))
        self.computer_score_label.pack()

        self.result_label = Label(self.root, text="", font=("Futura", 12))
        self.result_label.pack()

        self.rock_button = Button(self.root, text="Rock", command=self.rock)
        self.rock_button.pack()

        self.paper_button = Button(self.root, text="Paper", command=self.paper)
        self.paper_button.pack()

        self.scissors_button = Button(self.root, text="Scissors", command=self.scissors)
        self.scissors_button.pack()

        self.reset_button = Button(self.root, text="Reset", command=self.reset)
        self.reset_button.pack()

    def computer_choice(self):
        return choice(['rock', 'paper', 'scissors'])
        # 'choice' decides which of the following elements the computer will choose randomly

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            return "You win!"
        else:
            return "You lose!"

    def rock(self):
        computer_choice = self.computer_choice()
        result = self.determine_winner('rock', computer_choice)
        self.result_label['text'] = f"Computer chose: {computer_choice}\n{result}"
        # Updating of result: whether you lost or you win
        if result == "You win!":
            self.user_score += 1
            self.user_score_label['text'] = f"Your Score: {self.user_score}"
        elif result == "You lose!":
            self.computer_score += 1
            self.computer_score_label['text'] = f"Computer Score: {self.computer_score}"

    def paper(self):
        computer_choice = self.computer_choice()
        result = self.determine_winner('paper', computer_choice)
        self.result_label['text'] = f"Computer chose: {computer_choice}\n{result}"
        # Updating of result: whether you lost or you win
        if result == "You win!":
            self.user_score += 1
            self.user_score_label['text'] = f"Your Score: {self.user_score}"
        elif result == "You lose!":
            self.computer_score += 1
            self.computer_score_label['text'] = f"Computer Score: {self.computer_score}"

    def scissors(self):
        computer_choice = self.computer_choice()
        result = self.determine_winner('scissors', computer_choice)
        self.result_label['text'] = f"Computer chose: {computer_choice}\n{result}"
        if result == "You win!":
            self.user_score += 1
            self.user_score_label['text'] = f"Your Score: {self.user_score}"
        elif result == "You lose!":
            self.computer_score += 1
            self.computer_score_label['text'] = f"Computer Score: {self.computer_score}"

    def reset(self):
        self.user_score = 0
        self.computer_score = 0
        self.user_score_label['text'] = "Your Score: 0"
        self.computer_score_label['text'] = "Computer Score: 0"
        self.result_label['text'] = ""

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = RockPaperScissors()
    game.run()
