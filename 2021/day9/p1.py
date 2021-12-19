

def test1_CheckSumOfLowPoints(filename, expected):
    input = open(filename, 'r').readlines()
    result = GetSumOfLowPoints(input)
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

def GetSumOfLowPoints(matrix):
    MaxRows = len(matrix)
    MaxColumns = len(matrix[0].strip())
    total = 0
    for j in range(MaxRows):
        for i in range(MaxColumns):
            current = int(matrix[j][i])
            up = int(matrix[j - 1][i]) if j - 1 >= 0 else None
            down = int(matrix[j + 1][i]) if j + 1 < MaxRows else None
            left = int(matrix[j][i - 1]) if i - 1 >= 0 else None
            right = int(matrix[j][i + 1]) if i + 1 < MaxColumns else None
            if IsLowPoint(current, up, down, left, right):
                total += 1 + current
    return total

def main(filename):
    input = open(filename, 'r').readlines()
    total = GetSumOfLowPoints(input)
    print("Solution: {total}".format(total=total))

# testing
test1_CheckSumOfLowPoints('test.in', 15)

# program
main("input.in")