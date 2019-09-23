import random

def roll_dice(num):

    sumOf = 0

    for i in range(1, num+1):

        roll = random.randint(1,6)
        sumOf += roll

    return sumOf

print(roll_dice(2))
