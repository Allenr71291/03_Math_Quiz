from tkinter import *
from functools import partial


class Start:
    def __init__(self, parent):

        background_color = "#78ffd1"

        self.start_frame = Frame(pady=10, padx=10)
        self.start_frame.grid()

        self.help_frame = Frame(pady=10, padx=10)
        self.help_frame.grid()

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
                                            wrap=275, justify=LEFT,
                                            padx=10, pady=10,)
        self.math_instructions.grid(row=1)

        self.question_frame = Frame(self.start_frame, width=10)
        self.question_frame.grid(row=2)

        self.entry_frame = Frame(self.start_frame, width=5)
        self.entry_frame.grid(row=3)

        self.add_questions_button = Label(self.question_frame,
                                       font="Arial 15 bold",
                                       text="Set Amount of Questions")
        self.add_questions_button.grid(row=0, column=0)

        self.start_amount_entry = Entry(self.question_frame,
                                        font="Arial 19 bold", width=10,)
        self.start_amount_entry.grid(row=0, column=1)

        self.amount_error_label = Label(self.question_frame, fg="maroon",
                                        text="", font="Arial 10 bold", wrap=275,
                                        justify=LEFT)
        self.amount_error_label.grid(row=1, columnspan=2, pady=5)

        self.numbers_between_button = Label(self.entry_frame,
                                       font="Arial 15 bold",
                                       text="Use numbers between")
        self.numbers_between_button.grid(row=2, column=0)

        self.start_amount_entry1 = Entry(self.entry_frame,
                                        font="Arial 19 bold", width=5)
        self.start_amount_entry1.grid(row=2, column=1, padx=20)

        self.numbers_between_button = Label(self.entry_frame,
                                       font="Arial 15 bold",
                                       text="and")
        self.numbers_between_button.grid(row=2, column=2)

        self.start_amount_entry2 = Entry(self.entry_frame,
                                        font="Arial 19 bold", width=5)
        self.start_amount_entry2.grid(row=2, column=3, padx=20)

        self.numbers_error_label = Label(self.question_frame, fg="maroon",
                                        text="", font="Arial 10 bold", wrap=275, justify=LEFT)
        self.numbers_error_label.grid(row=3, columnspan=2, pady=5)

        # button frame (row 3)
        self.stakes_frame = Frame(self.start_frame)
        self.stakes_frame.grid(row=4)

        # Buttons here:
        button_font = "Arial 12 bold"

        # Orange low stakes button
        self.multiplication_button = Button(self.stakes_frame, text="Multiplication",
                                       command=lambda: self.to_quiz("*"),
                                       font=button_font, bg="#1170ed")
        self.multiplication_button.grid(row=0, column=0, pady=10)

        # Yellow Medium stakes button
        self.subtraction_button = Button(self.stakes_frame, text="Subtraction",
                                       command=lambda: self.to_quiz("-"),
                                       font=button_font, bg="#FFFF33")
        self.subtraction_button.grid(row=0, column=1, pady=10)

        # Green High Stakes button
        self.addition_button = Button(self.stakes_frame, text="Addition",
                                       command=lambda: self.to_quiz("+"),
                                       font=button_font, bg="#99FF33")
        self.addition_button.grid(row=0, column=2, pady=10)

        # help button
        self.help_button = Button(self.help_frame, text="How to Play",
                                       font=button_font, bg="#808080", fg="white",
                                       command=self.to_help)
        self.help_button.grid(row=1, column=1, pady=10)

    def to_quiz(self, stakes):
        # Number checking function
        starting_balance = self.start_amount_entry.get()
        # Game(self, stakes, starting_balance)

        error_back = "#ffafaf"
        has_errors = "no"

        self.start_amount_entry.config(bg="white")
        self.amount_error_label.config(text="")

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
                self.starting_funds.set(starting_balance)

        except ValueError:
            has_errors = "yes"
            error_feedback = "Please enter a whole number(no text / decimals)"

        if has_errors == "yes":
            self.start_amount_entry.config(bg=error_back)
            self.amount_error_label.config(text=error_feedback)

        else:
            self.starting_funds.set(starting_balance)

            starting_balance = self.starting_funds.get()

            Quiz(self, stakes, starting_balance)

        # hide start up menu disabled for testing purposes
        # root.withdraw()

    def to_help(self):
        get_help = Help(self)


class Quiz:
    def __init__(self, partner, stakes, starting_balance):
        print(stakes)
        print(starting_balance)


class Help:
    def __init__(self, partner):
        # Disable help button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (ie: help box)
        self.help_box = Toplevel()

        # If users press cross at top, closes help and "releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # set up help GUI Frame
        self.help_frame = Frame(self.help_box, width=300)
        self.help_frame.grid()

        # Set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                 font="arial 14 bold")
        self.how_heading.grid(row=0)

        help_text = "Help!"
        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text=help_text,
                               justify=LEFT, wrap=400, padx=10, pady=10)
        self.help_text.grid(row=1)

        # Dismiss Button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = Start(root)
    root.mainloop()