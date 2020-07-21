import random

NUM_QUES = 5
winnings = 0

numbers_used_low = 1
numbers_used_high = 8

cost = NUM_QUES * 5

for item in range(0, NUM_QUES):
    answer = ""
    round_winnings = 0

    for thing in range(0,3):

        prize_num = random.randint(1,4)
        answer += " "
        if prize_num == 1:
            answer += "gold"
            round_winnings +=5
        elif prize_num ==2:
            answer += "silver"
            round_winnings += 2
        elif prize_num == 3:
            answer += "copper"
            round_winnings += 1
        else:
            answer += "lead"

    print("You won {} which is worth {}".format(answer, round_winnings))
    winnings += round_winnings

print("Paid In: ${}".format(cost))
print("Pay Out: ${}".format(winnings))

if winnings > cost:
    print("You came out ${} ahead".format(winnings - cost))
else:
    print("Sorry, you lost ${}".format(cost-winnings))