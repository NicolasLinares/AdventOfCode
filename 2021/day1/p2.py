
def test(inputFloorReports, expectedIncreases, slideWindowSize):
    result = CalculateTotalIncreases(inputFloorReports, slideWindowSize)
    assert(result == expectedIncreases)

def CalculateTotalIncreases(floorReports, slideWindowSize):
    prev = None
    total = 0

    for i in range(len(floorReports) - slideWindowSize + 1):
        depthWindow = floorReports[i: i + slideWindowSize]
        depth = sum(map(int, depthWindow))
        if (prev is not None and prev < depth):
            total += 1
        prev = depth

    return total

def main(filename):
    input = open(filename, 'r')
    lines = input.readlines()

    slideWindowSize = 3
    total = CalculateTotalIncreases(lines, slideWindowSize)
    print("Solution: {totalIncreases}".format(totalIncreases=total))

# testing
test([199, 200, 208, 210, 200, 207, 240, 269, 260, 263], 5, 3)

# Program
main('input.in')