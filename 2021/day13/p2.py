import re
import pdb

def test1_CheckFolds(filename, expected):
    input = open(filename, 'r').readlines()
    (points, instructions) = ParseInput(input)
    result = Fold(points, instructions)
    assert(result == expected)

X_AXIS = 'x'
Y_AXIS = 'y'

def ParseStep(step):
    step = re.match(".*([xy])=(\\d+)", step)
    axis, point = 'x', 0
    if step:
        axis = step.group(1)
        point = int(step.group(2))
    return (axis, point)

def StrToPointXY(pointStr):
    point = pointStr.split(',')
    x = int(point[0])
    y = int(point[1])
    return (x, y)

def PointXYToStr(x, y):
    return "{x},{y}".format(x=x, y=y)

def PrintCode(pointsSet):
    max_x = -1
    max_y = -1
    for p in pointsSet:
        (x, y) = StrToPointXY(p)
        if (x > max_x):
            max_x = x
        if (y > max_y):
            max_y = y     
    max_x += 1
    max_y += 1
    display = [[' ' for x in range(max_x)] for y in range(max_y)] 
    for p in pointsSet:
        (x, y) = StrToPointXY(p)
        display[y][x] = '#'

    for y in range(max_y):
        for x in range(max_x):
            print(display[y][x], end=' ')
        print()

def Fold(points, instructions):
    pointsSet = set(points)
    auxPointSet = set()
    for step in instructions:
        (axis, fold) = ParseStep(step)

        for pointStr in pointsSet:
            (x, y) = StrToPointXY(pointStr)
            if axis == Y_AXIS and fold < y:
                y = fold - (y - fold)
            if axis == X_AXIS and fold < x:
                x = fold - (x - fold)
            pointStr = PointXYToStr(x, y)
            auxPointSet.add(pointStr)

        pointsSet.clear()
        pointsSet.update(auxPointSet)
        auxPointSet.clear()


    PrintCode(pointsSet)

    return len(pointsSet)

def ParseInput(input):
    points = []
    instructions = []
    for line in input:            
        if re.match("\\d+,\\d+", line):
            pointStr = line.strip()
            points.append(pointStr)
        elif line != '\n':
            instructions.append(line.strip())

    return (points, instructions)

def main(filename):
    input = open(filename, 'r').readlines()
    (points, instructions) = ParseInput(input)
    total = Fold(points, instructions)
    print("Solution: {total}".format(total=total))

# testing
# test1_CheckFolds('test.in', 16)

# program
main("input.in")