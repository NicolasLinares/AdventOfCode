
def test1_CheckNumberOfFlashes(filename, expected):
    input = open(filename, 'r').readlines()
    STEPS = 100
    result = CalculateTotalFlashes(input, STEPS)
    assert(result == expected)


def StringArraysToMatrix(input):
    matrix = input
    for i in range(len(input)):
        matrix[i] = [int(num) for num in input[i].strip()]
    return matrix

FLASHED_OCTOPUS = 0

def IsInsideLimits(octopuses, j, i):
    MaxRows = len(octopuses)
    MaxColumns = len(octopuses[0])
    return 0 <= j < MaxRows and 0 <= i < MaxColumns

def ExpandAdjacentFlashes(octopuses, j, i):
    expand = []
    for x in range(j-1, j+1 + 1):
        for y in range(i-1, i+1 + 1):
            if IsInsideLimits(octopuses, x, y):
                if (octopuses[x][y] != FLASHED_OCTOPUS):
                    octopuses[x][y] = (octopuses[x][y] + 1) % 10
                    if octopuses[x][y] == FLASHED_OCTOPUS:
                        expand.append((x, y))
    return (expand, octopuses)

def ExpandAllFlashes(expand, octopuses):
    flashes = len(expand)
    if flashes == 0:
        return (0, octopuses)

    newToExpand = []
    for ex in expand:
        j, i = ex[0], ex[1]
        (toExpand, octopuses) = ExpandAdjacentFlashes(octopuses, j, i)
        newToExpand = [*newToExpand, *toExpand]

    (newFlashes, octopuses) = ExpandAllFlashes(newToExpand, octopuses)

    return (newFlashes + flashes, octopuses)

def CalculateTotalFlashes(input, steps):
    octopuses = StringArraysToMatrix(input)
    MaxRows = len(octopuses)
    MaxColumns = len(octopuses[0])
    totalFlashes = 0
    for step in range(steps):
        expand = []
        for j in range(MaxRows):
            for i in range(MaxColumns):
                octopuses[j][i] = (octopuses[j][i] + 1) % 10
                if octopuses[j][i] == FLASHED_OCTOPUS:
                    expand.append([j, i])

        (flashes, octopuses) = ExpandAllFlashes(expand, octopuses)
        totalFlashes += flashes

    return totalFlashes

def main(filename):
    input = open(filename, 'r').readlines()
    STEPS = 100
    total = CalculateTotalFlashes(input, STEPS)
    print("Solution: {total}".format(total=total))

# testing
test1_CheckNumberOfFlashes('test.in', 1656)

# program
main("input.in")