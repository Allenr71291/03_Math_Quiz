from tkinter import *
from functools import partial


class Start:
    def __init__(self, parent):

        self.start_frame = Frame(pady=10, padx=10)
        self.start_frame.grid()

        self.starting_funds = IntVar()
        self.starting_funds.set(0)

        self.math_quiz_label = Label(self.start_frame,
                                          text="Math Quiz",
                                          font=("Arial", "19", "bold"),
                                          padx=10, pady=10)
        self.math_quiz_label.grid(row=0)

        self.math_instructions = Label(self.start_frame, font="Arial 10 italic",
                                       text="Please enter the number of "
                                            "questions you would like to "
                                            "answer in the box below. Keep "
                                            "in mind that you cant have less "
                                            "than 0 questions!",
                                            wrap=275, justify=LEFT, padx=10, pady=10)
        self.math_instructions.grid(row=1)

        self.question_frame = Frame(self.start_frame, width=10)
        self.question_frame.grid(row=2)

        self.start_amount_entry = Entry(self.question_frame,
                                        font="Arial 19 bold", width=10)
        self.start_amount_entry.grid(row=0, column=0)

        self.add_funds_button = Button(self.question_frame,
                                       font="Arial 15 bold",
                                       text="Set Amount of Questions",
                                       command=self.check_funds)
        self.add_funds_button.grid(row=0, column=1)

        self.amount_error_label = Label(self.question_frame, fg="maroon",
                                        text="", font="Arial 10 bold", wrap=275,
                                        justify=LEFT)
        self.amount_error_label.grid(row=1, columnspan=2, pady=5)

        # button frame (row 3)
        self.stakes_frame = Frame(self.start_frame)
        self.stakes_frame.grid(row=3)

        # Buttons here:
        button_font = "Arial 12 bold"

        # Orange low stakes button
        self.low_stakes_button = Button(self.stakes_frame, text="Multiplication",
                                       command=lambda: self.to_quiz("*"),
                                       font=button_font, bg="#FF9933")
        self.low_stakes_button.grid(row=0, column=0, pady=10)

        # Yellow Medium stakes button
        self.medium_stakes_button = Button(self.stakes_frame, text="Subtraction",
                                       command=lambda: self.to_quiz("-"),
                                       font=button_font, bg="#FFFF33")
        self.medium_stakes_button.grid(row=0, column=1, pady=10)

        # Green High Stakes button
        self.high_stakes_button = Button(self.stakes_frame, text="Addition",
                                       command=lambda: self.to_quiz("+"),
                                       font=button_font, bg="#99FF33")
        self.high_stakes_button.grid(row=0, column=2, pady=10)

        # Disabling buttons
        self.low_stakes_button.config(state=DISABLED)
        self.medium_stakes_button.config(state=DISABLED)
        self.high_stakes_button.config(state=DISABLED)

        # help button
        self.help_button = Button(self.stakes_frame, text="How to Play",
                                       font=button_font, bg="#808080", fg="white")
        self.help_button.grid(row=1, column=1, pady=10)

    # Number checking function
    def check_funds(self):
        starting_balance = self.start_amount_entry.get()
        # Game(self, stakes, starting_balance)

        error_back = "#ffafaf"
        has_errors = "no"

        self.start_amount_entry.config(bg="white")
        self.amount_error_label.config(text="")

        # Disabling buttons
        self.low_stakes_button.config(state=DISABLED)
        self.medium_stakes_button.config(state=DISABLED)
        self.high_stakes_button.config(state=DISABLED)

        try:
            starting_balance = int(starting_balance)

            if starting_balance <= 0:
                has_errors = "yes"
                error_feedback = "Sorry, the smallest amount of " \
                                 "questions you can play with is 1"
            elif starting_balance > 50:
                has_errors = "yes"
                error_feedback = "You cannot play with more than 50 " \
                                 "Questions!"

            elif starting_balance >= 1:
                # Enable all buttons
                self.low_stakes_button.config(state=NORMAL)
                self.medium_stakes_button.config(state=NORMAL)
                self.high_stakes_button.config(state=NORMAL)

        except ValueError:
            has_errors= "yes"
            error_feedback = "Please enter a whole number(no text / decimals)"

        if has_errors == "yes":
            self.start_amount_entry.config(bg=error_back)
            self.amount_error_label.config(text=error_feedback)

        else:
            self.starting_funds.set(starting_balance)

    def to_quiz(self, stakes):

        starting_balance = self.starting_funds.get()

        Quiz(self, stakes, starting_balance)

        # hide start up menu disabled for testing purposes
        # root.withdraw()


class Quiz:
    def __init__(self, partner, stakes, starting_balance):
        print(stakes)
        print(starting_balance)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = Start(root)
    root.mainloop()