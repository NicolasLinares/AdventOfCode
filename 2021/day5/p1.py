

def test1_IsHorizontal(input, expected):
    input = TranslateInputToCloudLine(input)
    result = IsHorizontal(input)
    assert(result == expected)

def test2_IsVertical(input, expected):
    input = TranslateInputToCloudLine(input)
    result = IsVertical(input)
    assert(result == expected)

def test3_AreEquals(input1, input2, expected):
    input1 = TranslateInputToCloudLine(input1)
    input2 = TranslateInputToCloudLine(input2)
    result = AreEquals(input1, input2)
    assert(result == expected)

def test4_IsShortestThan(input1, input2, expected):
    input1 = TranslateInputToCloudLine(input1)
    input2 = TranslateInputToCloudLine(input2)
    expected = TranslateInputToCloudLine(expected)
    (shortest, largest) = GetShortest(input1, input2)
    assert(AreEquals(shortest, expected) == True)
 
def test5_DistanceShouldBe(input, expected):
    input = TranslateInputToCloudLine(input)
    result = GetDistance(input)
    assert(result == expected)

def test6_ContainsPoint(input1, input2, expected):
    input1 = TranslateInputToCloudLine(input1)
    result = ContainsPoint(input1, input2)
    assert(result == expected)


class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __repr__(self):
        return "({x},{y})".format(x=self.x, y=self.y)


class CloudLine:
    def __init__(self, pointA, pointB):
        self.pA = pointA
        self.pB = pointB
    def __repr__(self):
        return "{pSrc} -> {pDst}\n".format(pSrc=self.pA, pDst=self.pB)


def IsVertical(l1):
    return l1.pA.x == l1.pB.x

def IsHorizontal(l1):
    return l1.pA.y == l1.pB.y

def AreEquals(l1, l2):
    return str(l1) == str(l2)

def GetDistance(l1):
    x1 = l1.pA.x
    y1 = l1.pA.y
    x2 = l1.pB.x
    y2 = l1.pB.y
    return int((((x2 - x1 )**2) + ((y2-y1)**2) )**0.5)

def GetShortest(l1, l2):
    l1Dist = GetDistance(l1)
    l2Dist = GetDistance(l2)
    return (l1, l2) if (l1Dist <= l2Dist) else (l2, l1)

def ContainsPoint(l1, p):
    x1 = l1.pA.x
    y1 = l1.pA.y
    x2 = l1.pB.x
    y2 = l1.pB.y
    x3 = p.x
    y3 = p.y

    return (x1 <= x3 <= x2 and y1 <= y3 <= y2) or (x2 <= x3 <= x1 and y2 <= y3 <= y1)
     

def TranslateInputToCloudLine(line):
    segment = line.split(' -> ')
    pA = segment[0].split(',')
    pA = Point(pA[0], pA[1])
    pB = segment[1].split(',')
    pB = Point(pB[0], pB[1])

    return CloudLine(pA, pB)

def GetHorizontalAndVerticalClouds(lines):
    clouds = []
    for line in lines:
        cloudLine = TranslateInputToCloudLine(line)
        if (IsHorizontal(cloudLine) or IsVertical(cloudLine)):
            clouds.append(cloudLine)
    return clouds

def GetRange(a, b):
    return (a, b) if  a <= b else (b, a)

def AddIfContains(pointsDict, point, largest):
    if ContainsPoint(largest, point):
        str_point = str(point)
        if str_point in pointsDict:
            pointsDict[str_point] += 1
        else:
            pointsDict[str_point] = 1
    return pointsDict

def GetPointsContained(pointsDict, shortest, largest):
    
    if (IsHorizontal(shortest)):
        (i, N) = GetRange(shortest.pA.x, shortest.pB.x)
        keepValue = shortest.pA.y
        while (i <= N):
            point = Point(i, keepValue)
            pointsDict = AddIfContains(pointsDict, point, largest)
            i += 1
    else:
        (i, N) = GetRange(shortest.pA.y, shortest.pB.y)
        keepValue = shortest.pA.x
        while (i <= N):
            point = Point(keepValue, i)
            pointsDict = AddIfContains(pointsDict, point, largest)
            i += 1

    return pointsDict



def GetNumberOfPointsWithAtLeastTwoLinesOverlap(lines):
    clouds = GetHorizontalAndVerticalClouds(lines)

    pointsDict = dict()
    for cl1 in clouds:
        for cl2 in clouds:
            if not AreEquals(cl1, cl2):
                (shortestCloud, largestCloud) = GetShortest(cl1, cl2)
                pointsDict = GetPointsContained(pointsDict, shortestCloud, largestCloud)

    return len(pointsDict)

def main(filename):
    input = open(filename, 'r')
    lines = input.readlines()
    total = GetNumberOfPointsWithAtLeastTwoLinesOverlap(lines)
    print("Solution: {total}".format(total=total))

# testing
test1_IsHorizontal('1,1 -> 1,3', False)
test1_IsHorizontal('0,9 -> 5,9', True)

test2_IsVertical('1,1 -> 1,3', True)
test2_IsVertical('0,9 -> 2,9', False)

test3_AreEquals('0,9 -> 2,9', '0,9 -> 2,9', True)
test3_AreEquals('1,9 -> 2,9', '0,9 -> 2,9', False)

test4_IsShortestThan('1,9 -> 2,9', '0,9 -> 2,9', '1,9 -> 2,9')

test5_DistanceShouldBe('0,9 -> 5,9', 5)
test5_DistanceShouldBe('1,9 -> 2,9', 1)
test5_DistanceShouldBe('0,9 -> 2,9', 2)
test5_DistanceShouldBe('2,9 -> 0,9', 2)

test6_ContainsPoint('1,9 -> 2,9', Point(1,9), True)
test6_ContainsPoint('2,9 -> 1,9', Point(1,9), True)
test6_ContainsPoint('2,9 -> 2,9', Point(1,9), False)
test6_ContainsPoint('2,9 -> 2,9', Point(3,9), False)

# program
main("input.in")




# Strategy:
# - cojo dos líneas <- Mejora: descartar la comprobación si se encuentran alejadas  
# - cojo la línea más corta de las dos que comparo
# - y la recorro comprobando si cada punto se encuentra dentro de la otra
# - si un punto coincide lo registro en un hash
# - el resultado final debe ser el número de puntos registrados en ese hash
# - además tendría en cada entrada de ese hash el número de líneas que se han superpuesto en ese punto,
#   es decir, el grosor de esas líneas de nubes.