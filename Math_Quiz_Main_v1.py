from tkinter import *
from functools import partial


class Start:
    def __init__(self, parent):

        background_color = "#78ffd1"

        self.start_frame = Frame(pady=10, padx=10)
        self.start_frame.grid()

        self.help_frame = Frame(pady=10, padx=10)
        self.help_frame.grid()

        self.number_questions = IntVar()
        self.number_questions.set(0)

        self.numbers_used_low = IntVar()
        self.numbers_used_low.set(0)

        self.numbers_used_high = IntVar()
        self.numbers_used_high.set(0)

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

        # Number of questions
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

        # Low number entry box
        self.numbers_used_entry_low = Entry(self.entry_frame,
                                        font="Arial 19 bold", width=5)
        self.numbers_used_entry_low.grid(row=2, column=1, padx=20)

        self.numbers_between_button = Label(self.entry_frame,
                                       font="Arial 15 bold",
                                       text="and")
        self.numbers_between_button.grid(row=2, column=2)

        # high number entry box
        self.numbers_used_entry_high = Entry(self.entry_frame,
                                        font="Arial 19 bold", width=5)
        self.numbers_used_entry_high.grid(row=2, column=3, padx=20)

        self.numbers_error_label = Label(self.question_frame, fg="maroon",
                                        text="", font="Arial 10 bold", wrap=275, justify=LEFT)
        self.numbers_error_label.grid(row=3, columnspan=2, pady=5)

        # button frame (row 3)
        self.question_type_frame = Frame(self.start_frame)
        self.question_type_frame.grid(row=4)

        # Buttons here:
        button_font = "Arial 12 bold"

        # Orange low question_type button
        self.multiplication_button = Button(self.question_type_frame, text="Multiplication",
                                       command=lambda: self.to_quiz("*"),
                                       font=button_font, bg="#1170ed")
        self.multiplication_button.grid(row=0, column=0, pady=10)

        # Yellow Medium question_type button
        self.subtraction_button = Button(self.question_type_frame, text="Subtraction",
                                       command=lambda: self.to_quiz("-"),
                                       font=button_font, bg="#FFFF33")
        self.subtraction_button.grid(row=0, column=1, pady=10)

        # Green High question_type button
        self.addition_button = Button(self.question_type_frame, text="Addition",
                                       command=lambda: self.to_quiz("+"),
                                       font=button_font, bg="#99FF33")
        self.addition_button.grid(row=0, column=2, pady=10)

        # help button
        self.help_button = Button(self.help_frame, text="How to Play",
                                       font=button_font, bg="#808080", fg="white",
                                       command=self.to_help)
        self.help_button.grid(row=1, column=1, pady=10)

    def to_quiz(self, question_type):
        # Number checking function
        question_amount = self.start_amount_entry.get()


        error_back = "#ffafaf"
        has_errors = "no"

        self.start_amount_entry.config(bg="white")
        self.amount_error_label.config(text="")

        try:
            question_amount = int(question_amount)

            if question_amount <= 0:
                has_errors = "yes"
                error_feedback = "Sorry, the smallest amount of " \
                                 "questions you can play with is 1"
            elif question_amount > 50:
                has_errors = "yes"
                error_feedback = "You cannot play with more than 50 " \
                                 "Questions!"

            elif question_amount >= 1:
                self.number_questions.set(question_amount)

        except ValueError:
            has_errors = "yes"
            error_feedback = "Please enter a whole number(no text / decimals)"

        if has_errors == "yes":
            self.start_amount_entry.config(bg=error_back)
            self.amount_error_label.config(text=error_feedback)

        else:

            numbers_used_low = self.numbers_used_entry_low.get()

            error_back = "#ffafaf"
            has_errors = "no"

            self.start_amount_entry.config(bg="white")
            self.amount_error_label.config(text="")

            try:
                numbers_used_low = int(numbers_used_low)

                if numbers_used_low <= 0:
                    has_errors = "yes"
                    error_feedback = "Sorry, the smallest amount of " \
                                     "questions you can play with is 1"
                elif numbers_used_low > 50:
                    has_errors = "yes"
                    error_feedback = "You cannot play with more than 50 " \
                                     "Questions!"

                elif numbers_used_low >= 1:
                    self.numbers_used_low.set(numbers_used_low)

            except ValueError:
                has_errors = "yes"
                error_feedback = "Please enter a whole number(no text / decimals)"

            if has_errors == "yes":
                self.start_amount_entry.config(bg=error_back)
                self.amount_error_label.config(text=error_feedback)

            else:

                numbers_used_high = self.numbers_used_entry_high.get()

                error_back = "#ffafaf"
                has_errors = "no"

                self.start_amount_entry.config(bg="white")
                self.amount_error_label.config(text="")

                try:
                    numbers_used_high = int(numbers_used_high)

                    if numbers_used_high <= 0:
                        has_errors = "yes"
                        error_feedback = "Sorry, the smallest amount of " \
                                         "questions you can play with is 1"
                    elif numbers_used_high > 50:
                        has_errors = "yes"
                        error_feedback = "You cannot play with more than 50 " \
                                         "Questions!"

                    elif numbers_used_high >= 1:
                        self.numbers_used_high.set(numbers_used_high)

                except ValueError:
                    has_errors = "yes"
                    error_feedback = "Please enter a whole number(no text / decimals)"

                if has_errors == "yes":
                    self.start_amount_entry.config(bg=error_back)
                    self.amount_error_label.config(text=error_feedback)

                else:

                    # code for starting game:
                    self.number_questions.set(question_amount)

                    question_amount = self.number_questions.get()
                    numbers_used_low = self.numbers_used_low.get()
                    numbers_used_high = self.numbers_used_high.get()

                    Quiz(self, question_type, question_amount, numbers_used_high, numbers_used_low)

        # hide start up menu disabled for testing purposes
        # root.withdraw()

    def to_help(self):
        get_help = Help(self)


class Quiz:
    def __init__(self, partner, question_type, question_amount, numbers_used_low,
                 numbers_used_high):

        print(question_type)
        print(question_amount)
        print(numbers_used_low)
        print(numbers_used_high)
        self.balance = IntVar()

        self.balance.set(starting_balance)

        self.multiplier = IntVar()
        self.multiplier.set(stakes)

        # GUI Setup
        self.game_box = Toplevel()

        # If user cross at top, game quits
        self.game_box.protocol('WM_DELETE_WINDOW', self.to_quit)

        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # Heading Row
        self.heading_label = Label(self.game_frame, text="Play...",
                                   font="Arial 24 bold", padx=10,
                                   pady=10)
        self.heading_label.grid(row=0)

        # Instructions Label
        self.instructions_label = Label(self.game_frame, wrap=300, justify=LEFT,
                                        text="Press <enter> or click the 'Open "
                                        "Boxes' button to reveal the "
                                        "contents of the mystery boxes.",
                                        font="Arial 10", padx=10, pady=10)
        self.instructions_label.grid(row=1)

        # Boxes go here (row 2)
        box_text = "Arial 16 bold"
        box_back = "#b9ea96" # light green
        box_width = 5
        self.box_frame = Frame(self.game_frame)
        self.box_frame.grid(row=2, pady=10)

        self.prize1_label = Label(self.box_frame, text="?\n", font=box_text,
                                  bg=box_back, width=box_width, padx=10, pady=10)
        self.prize1_label.grid(row=0, column=0)

        self.prize2_label = Label(self.box_frame, text="?\n", font=box_text,
                                  bg=box_back, width=box_width, padx=10, pady=10)
        self.prize2_label.grid(row=0, column=1, padx=10)

        self.prize3_label = Label(self.box_frame, text="?\n", font=box_text,
                                  bg=box_back, width=box_width, padx=10, pady=10)
        self.prize3_label.grid(row=0, column=2)

        # Play button goes here (row 3)
        self.play_button = Button(self.game_frame, text="Open Boxes",
                                  bg="#FFF333", font="Arial 15 bold", width=20,
                                  padx=10, pady=10, command=self.reveal_boxes)
        self.play_button.grid(row=3)

        self.play_button.focus()
        self.play_button.bind('<Return>', lambda e: self.reveal_boxes())
        self.play_button.grid(row=3)

        # Balance Label (row 4)

        start_text = "Game Cost: ${} \n "" \nHow Much " \
                     "will you win?".format(stakes * 5)

        self.balance_label = Label(self.game_frame, font="Arial 12 bold", fg="green",
                                   text=start_text, wrap=300,
                                   justify=LEFT)
        self.balance_label.grid(row=4, pady=10)

        # Help and Game Stats button (row 5)
        self.help_export_frame = Frame(self.game_frame)
        self.help_export_frame.grid(row=5, pady=10)

        self.help_button = Button(self.help_export_frame, text="Help / Rules",
                                  font="Arial 15 bold",
                                  bg="#808080", fg="white")
        self.help_button.grid(row=0, column=0, padx=2)

        self.stats_button = Button(self.help_export_frame, text="Game Stats....",
                                   font="Arial 15 bold",
                                   bg="#003366", fg="white")
        self.stats_button.grid(row=0, column=1, padx=2)

        # Quit button
        self.quit_button = Button(self.game_frame, text="Quit", fg="white",
                                  bg="#660000", font="Arial 15 bold", width=20,
                                  command=self.to_quit, padx=10, pady=10)
        self.quit_button.grid(row=6, pady=10)

    def reveal_boxes(self):

        current_balance = self.balance.get()
        stakes_multiplier = self.multiplier.get()

        round_winnings = 0
        prizes = []
        backgrounds = []
        for thing in range(0, 3):
            prize_num = random.randint(1, 100)

            if 0 < prize_num <= 5:
                prize = "gold\n(${})".format(5* stakes_multiplier)
                back_color = "#CEA935"  # gold colour
                round_winnings += 5 * stakes_multiplier
            elif 1 < prize_num <= 25:
                prize = "silver\n(${})".format(2 * stakes_multiplier)
                back_color = "#B7B7B5"  # silver colour
                round_winnings += 2 * stakes_multiplier
            elif 3 < prize_num <= 65:
                prize = "copper\n(${})".format(1 * stakes_multiplier)
                back_color = "#BC7F61"  # copper colour
                round_winnings += 1 * stakes_multiplier
            else:
                prize = "lead\n($0)"
                back_color = "#595E71"  # lead colour

            prizes.append(prize)
            backgrounds.append(back_color)

        # Display prizes...
        self.prize1_label.config(text=prizes[0], bg=backgrounds[0])

        self.prize2_label.config(text=prizes[1], bg=backgrounds[1])

        self.prize3_label.config(text=prizes[2], bg=backgrounds[2])

        # Deduct cost of game
        current_balance -= 5 * stakes_multiplier

        # Add Winnings
        current_balance += round_winnings

        # Set balance to new balance
        self.balance.set(current_balance)

        balance_statement = "Game Cost: ${}\nPayback: ${} \n" \
                            "Current Balance: ${}".format(5 * stakes_multiplier,
                                                          round_winnings,
                                                          current_balance)

        # Edit label so user can see their balance
        self.balance_label.configure(text=balance_statement)

        if current_balance < 5 * stakes_multiplier:
            self.play_button.config(state=DISABLED)
            self.game_box.focus()
            self.play_button.config(text="Game Over")

            balance_statement = "Current Balance: ${}\n" \
                                "Your balance is too low. You can only quit " \
                                "or view your stats. Sorry about that.".format(current_balance)
            self.balance_label.config(fg="#660000", font="Arial 10 bold",
                                      text=balance_statement)

    def to_quit(self):
        root.destroy()


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