

def test1_CheckMinFuel(input, expected):
    result = GetMinFuel(input)
    assert(result == expected)

def GetMinMaxValues(input):
    min = input[0]
    max = input[0]
    for i in range(len(input)):
        if input[i] < min:
            min = input[i]
        if input[i] > max:
            max = input[i]
    return (min, max)

def GetMinFuel(input):

    (min, max) = GetMinMaxValues(input)

    minFuelPosition = 0
    minFuel = -1
    for finalPosition in range(min, max + 1):
        fuel = 0
        for initialPosition in range(len(input)):
            fuel += abs(input[initialPosition] - finalPosition)

        if (fuel < minFuel or minFuel == -1):
            minFuel = fuel
            minFuelPosition = finalPosition

    return minFuel

def main(filename):
    input = open(filename, 'r').read().split(',')
    input = [int(d) for d in input]
    total = GetMinFuel(input)
    print("Solution: {total}".format(total=total))

# testing
test1_CheckMinFuel([16,1,2,0,4,2,7,1,2,14], 37)

# program
main("input.in")