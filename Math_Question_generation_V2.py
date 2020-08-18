import random


numbers_used_low = 1
numbers_used_high = 8
operator = "*"
display_op = "×"



# generate question
num_1 = random.randint(numbers_used_low, numbers_used_high)
num_2 = random.randint(numbers_used_low, numbers_used_high)

question = "{} {} {}".format(num_1, operator, num_2)
display_question = "{} {} {} = ".format(num_1, display_op, num_2)
answer = eval(question)

print("{} {}".format(display_question, answer))
