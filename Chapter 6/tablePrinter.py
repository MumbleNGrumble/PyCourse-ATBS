# Practice Project - Table Printer


def printTable(table):
    '''Assumes that all the inner lists will contain the same number of strings.'''
    # Find the number of dimensions to print.
    cols = len(table)
    rows = len(table[0])

    # Find the longest string length in each column.
    colWidths = [0] * len(table)

    for i, column in enumerate(table):
        for string in column:
            if colWidths[i] < len(string):
                colWidths[i] = len(string)

    # Output table.
    for i in range(rows):
        output = ""

        for j in range(cols):
            output += table[j][i].rjust(colWidths[j]) + " "

        print(output.rstrip())


# Tests
# tableData = [['apples', 'oranges', 'cherries', 'banana'],
#              ['Alice', 'Bob', 'Carol', 'David'],
#              ['dogs', 'cats', 'moose', 'goose']]

# printTable(tableData)
