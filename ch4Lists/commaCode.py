def commaCode(sampleList):
    stringCode = ''
    if sampleList != [] and len(sampleList) != 1:
        for i in sampleList[:-1]:
            stringCode = stringCode + i + ', '
        stringCode = stringCode + 'and ' + sampleList[-1]
    elif len(sampleList) == 1:
        stringCode = sampleList[0]
    return stringCode


spam = ['apples', 'bananas', 'tofu', 'cats']
print('spam list is:', spam)
print('commaCode on spam is:', commaCode(spam))
emptyList = []
print('emptyList is:', emptyList)
print('commaCode on emptyList is:', commaCode(emptyList))
twoItems = ['apples', 'bananas']
print('twoItems list is:', twoItems)
print('commaCode on twoItems is:', commaCode(twoItems))
oneItem = ['apples']
print('oneItem list is:', oneItem)
print('commaCode on oneItem is:', commaCode(oneItem))
