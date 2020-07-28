import random

numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    randomList = []
    for flip in range(100):
        randomList.append(random.randint(0, 1))
    # Code that checks if there is a streak of 6 heads or tails in a row.
    for i in range(100):
        if randomList[i:i+6] == [0, 0, 0, 0, 0, 0]:
            numberOfStreaks += 1
            break
        elif randomList[i:i+6] == [1, 1, 1, 1, 1, 1]:
            numberOfStreaks += 1
            break

print('Chance of streak: %s%%' % (numberOfStreaks / 100))