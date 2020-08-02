tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    width = len(tableData)
    height = len(tableData[0])
    colWidths = [0] * width
    # iterate through each list to find longest string
    for x in range(width):
        for item in tableData[x]:
            if len(item) > colWidths[x]:
                colWidths[x] = len(item)
    # use colWidths to print formatted table
    for y in range(height):
        for x in range(width):
            print(tableData[x][y].rjust(colWidths[x]), end=' ')
        print()


# 0,0 1,0 2,0
# 0,1 1,1 2,1
# 0,2 1,2 2,2
# 0,3 1,3 2,3


printTable(tableData)


