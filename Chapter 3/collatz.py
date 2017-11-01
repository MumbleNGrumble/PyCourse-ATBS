# Practice Project - The Collatz Sequence


def collatzRecursive(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1

    print(result)

    if result == 1:
        return(result)
    else:
        collatzRecursive(result)


def collatzWhile(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1

    print(result)
    return(result)


# Prompt user for a starting number.
while True:
    try:
        startingNum = int(
            input('Provide a starting number for the Collatz sequence.\n'))
        break
    except ValueError:
        print('Must enter an integer.')

# Solving the problem recursively.
collatzRecursive(startingNum)

# Solving the problem with a while loop.
output = startingNum
while output != 1:
    output = collatzWhile(output)
