import random

def generateList():
    randomList = []
    for flip in range(100):
        randomList.append(random.randint(0, 1))
    return randomList


def findNumberOfStreaks(randomList):
    numberOfStreaks = 0
    # print(randomList)
    while len(randomList) >= 6:
        # print('randomList[0:6] is', randomList[0:6])
        if randomList[0:6] == [0, 0, 0, 0, 0, 0] or randomList[0:6] == [1, 1, 1, 1, 1, 1]:
            numberOfStreaks += 1
            # print('inside if')
            # print('numberofstreaks is ', numberOfStreaks)
        del randomList[0]
        # print('randomList is ', randomList)
        # print('len randomList is ', len(randomList))
    return numberOfStreaks

def findStreak(randomList):
    # print(randomList)
    while len(randomList) >= 6:
        # print('randomList[0:6] is', randomList[0:6])
        if randomList[0:6] == [0, 0, 0, 0, 0, 0] or randomList[0:6] == [1, 1, 1, 1, 1, 1]:
            return True
        del randomList[0]
    return False
# headList = [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0]
# tailList = [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
# newList = [0, 1, 1, 0, 1, 0, 1, 1, 1, 0]
# print(findStreak(headList))
# print('-------')
# print(findStreak(tailList))
# print('-------')
# print(findStreak(newList))
numberOfStreaks = 0
for experimentNumber in range(10000):
    if findStreak(generateList()):
        numberOfStreaks += 1
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
