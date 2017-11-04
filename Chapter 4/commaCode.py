# Practice Project - Comma Code


def addCommas(listInput):
    stringValue = ""

    if len(listInput) > 1:
        for item in listInput[:-1]:
            stringValue += str(item) + ", "

        stringValue += "and " + str(listInput[-1])
    else:
        stringValue = str(listInput[0])

    return stringValue

# Tests
# test1 = [1, 2, 3, 4, 5]
# test2 = ['apples', 'bananas', 'tofu', 'cats']
# test3 = ['one item']

# print(addCommas(test1))
# print(addCommas(test2))
# print(addCommas(test3))
