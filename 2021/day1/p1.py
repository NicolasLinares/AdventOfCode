
def test(inputFloorReports, expectedIncreases):
    result = CalculateTotalIncreases(inputFloorReports)
    assert(result == expectedIncreases)

def CalculateTotalIncreases(floorReports):
    prev = None
    total = 0
    for depth in floorReports:
        depth = int(depth)
        if (prev is not None and prev < depth):
            total += 1
        prev = depth

    return total

def main(filename):
    input = open(filename, 'r')
    lines = input.readlines()
    total = CalculateTotalIncreases(lines)
    print("Solution: {totalIncreases}".format(totalIncreases=total))

# testing
test([10, 11, 10, 11], 2)
test([10, 11, 10, 11, 11], 2)
test([10, 11, 10, 11, 11, 3, 2, 1], 2)
test([10, 11, 10, 11, 11, 3, 4, 2, 1], 3)

# Program
main('input.in')
