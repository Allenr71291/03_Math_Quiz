import random

NUM_QUES = 5
winnings = 0

numbers_used_low = 1
numbers_used_high = 8
operator = "*"
display_op = "×"

cost = NUM_QUES * 5

for item in range(0, NUM_QUES):

    # generate question
    num_1 = random.randint(numbers_used_low, numbers_used_high)
    num_2 = random.randint(numbers_used_low, numbers_used_high)

    question = "{} {} {}".format(num_1, operator, num_2)
    display_question = "{} {} {} = ".format(num_1, display_op, num_2)
    answer = eval(question)

    print("{} {}".format(display_question, answer))
