import numpy as np

def test1_CheckProdOfBasinSizes(filename, expected):
    input = open(filename, 'r').readlines()
    result = GetProdOfBasinSizes(input)
    assert(result == expected)

def IsLowPoint(current, up, down, left, right):
    if up != None and up <= current:
        return False
    if down != None and down <= current:
        return False
    if left != None and left <= current:
        return False
    if right != None and right <= current:
        return False
    return True

def GetMaxValues(array, amount):
    return sorted(array, reverse=True)[:amount]

DELIMITER = 9
VISITED = -1
def CalcBasinSize(matrix, j, i):
    MaxRows = len(matrix)
    MaxColumns = len(matrix[0])
    if j < 0 or j >= MaxRows or i < 0 or i >= MaxColumns:
        return 0
    current = int(matrix[j][i])
    if current == DELIMITER or current == VISITED:
        return 0
    matrix[j][i] = VISITED
    return 1 + CalcBasinSize(matrix, j - 1, i) + CalcBasinSize(matrix, j + 1, i) + CalcBasinSize(matrix, j, i - 1) + CalcBasinSize(matrix, j, i + 1)

def StringArraysToMatrix(input):
    matrix = input
    for i in range(len(input)):
        matrix[i] = [int(num) for num in input[i].strip()]
    return matrix

def GetProdOfBasinSizes(input):
    matrix = StringArraysToMatrix(input)
    MaxRows = len(matrix)
    MaxColumns = len(matrix[0])
    basins = []
    for j in range(MaxRows):
        for i in range(MaxColumns):
            current = int(matrix[j][i])
            up = int(matrix[j - 1][i]) if j - 1 >= 0 else None
            down = int(matrix[j + 1][i]) if j + 1 < MaxRows else None
            left = int(matrix[j][i - 1]) if i - 1 >= 0 else None
            right = int(matrix[j][i + 1]) if i + 1 < MaxColumns else None
            if IsLowPoint(current, up, down, left, right):
                auxMatrix = matrix
                basinSize = CalcBasinSize(auxMatrix, j, i)
                basins.append(basinSize)

    return np.prod(GetMaxValues(basins, 3))

def main(filename):
    input = open(filename, 'r').readlines()
    total = GetProdOfBasinSizes(input)
    print("Solution: {total}".format(total=total))

# testing
test1_CheckProdOfBasinSizes('test.in', 1134)

# program
main("input.in")