def test1_IsDiagonal(input, expected):
    input = TranslateInputToCloudLine(input)
    result = IsDiagonal(input)
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

def IsDiagonal(l1):
    return not IsVertical(l1) and not IsHorizontal(l1)


def TranslateInputToCloudLine(line):
    segment = line.split(' -> ')
    pA = segment[0].split(',')
    pA = Point(pA[0], pA[1])
    pB = segment[1].split(',')
    pB = Point(pB[0], pB[1])

    return CloudLine(pA, pB)

def GetAllClouds(lines):
    clouds = []
    for line in lines:
        cloudLine = TranslateInputToCloudLine(line)
        clouds.append(cloudLine)
    return clouds

def GetRange(a, b):
    return (a, b) if  a <= b else (b, a)


def GetNumberOfPointsWithAtLeastTwoLinesOverlap(lines):
    clouds = GetAllClouds(lines)

    w, h = 1000, 1000
    Matrix = [[0 for x in range(w)] for y in range(h)] 


    for cloud in clouds:
        
        if IsHorizontal(cloud):
            (i, N) = GetRange(cloud.pA.x, cloud.pB.x)
            keepValue = cloud.pA.y
            while (i <= N):
                Matrix[i][keepValue] += 1
                i += 1

        elif IsVertical(cloud):
            (i, N) = GetRange(cloud.pA.y, cloud.pB.y)
            keepValue = cloud.pA.x
            while (i <= N):
                Matrix[keepValue][i] += 1 
                i += 1

        else:

            N = abs(cloud.pA.x - cloud.pB.x)
            (leftPoint, rightPoint) = (cloud.pA, cloud.pB) if cloud.pA.x <= cloud.pB.x else (cloud.pB, cloud.pA)
            i, j = leftPoint.x, leftPoint.y
            N, M = rightPoint.x, rightPoint.y
            isUp = True if j <= M else False
            while (i <= N):
                Matrix[i][j] += 1 
                i += 1
                if isUp:
                    j += 1
                else:
                    j -= 1

    pointsDict = 0

    for i in range(w):
        for j in range(h):
            if (Matrix[i][j] > 1):
                pointsDict += 1

    return pointsDict

def main(filename):
    input = open(filename, 'r')
    lines = input.readlines()
    total = GetNumberOfPointsWithAtLeastTwoLinesOverlap(lines)
    print("Solution: {total}".format(total=total))

# testing

test1_IsDiagonal('1,1 -> 1,3', False)
test1_IsDiagonal('0,9 -> 2,9', False)
test1_IsDiagonal('872,108 -> 18,962', True)


# program
main("input.in")



