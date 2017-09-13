tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable():
    # initialise colWidths list with zeroes equal to tableData list length
    colWidths = [0] * len(tableData)

    # iterate over each list to find length of longest word, and set longest value
    # to i'th colWidths value
    for i in range(len(tableData)):
        for j in tableData[i]:
            if len(j) > colWidths[i]:
                colWidths[i] = len(j)

    #iterate over tableData and print justified items
    for x in range(len(tableData[0])):
        for y in range(len(tableData)):
            print(tableData[y][x].rjust(colWidths[y]), end = ' ')
        print(' ')
        
printTable()
