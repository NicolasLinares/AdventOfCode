

def CompleteTest(inputWire0, inputWire1, expectedData):
    centralPort = Point(0, 0)
    wire0 = createWire(centralPort, inputWire0)
    wire1 = createWire(centralPort, inputWire1)
    result = getClosestIntersection(wire0, wire1)
    assert(result == expectedData)

def IntersectTest(segV, segH, expectedData):
    result = hasIntersection(segV, segH)
    assert(result == expectedData)





class DIRECTION:
    LEFT = 'L'
    RIGHT = 'R'
    UP = 'U'
    DOWN = 'D'

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "({x},{y})".format(x=self.x, y=self.y)


class WireSegment:
    def __init__(self, pointA, pointB, dir, input):
        self.pA = pointA
        self.pB = pointB
        self.direction = dir
        self.input = input

    def __repr__(self):
        return "{dir}: {pSrc} -> {pDst}\n".format(pSrc=self.pA, pDst=self.pB, dir=self.direction)

def convertToArray(input):
    return input.split(",")

def calculateSegment(pointSrc, move):
    direction = move[0]
    offset = int(move[1:])
    if (direction == DIRECTION.UP):
        pointDst = Point(pointSrc.x, pointSrc.y + offset)
    if (direction == DIRECTION.DOWN):
        pointDst = Point(pointSrc.x, pointSrc.y - offset)
    if (direction == DIRECTION.LEFT):
        pointDst = Point(pointSrc.x - offset, pointSrc.y)
    if (direction == DIRECTION.RIGHT):
        pointDst = Point(pointSrc.x + offset, pointSrc.y)
    return WireSegment(pointSrc, pointDst, direction, move)


def filterByDirection(list):
    v = []
    h = []
    for i in list:
        if i.direction == DIRECTION.LEFT or i.direction == DIRECTION.RIGHT:
            h.append(i)
        elif i.direction == DIRECTION.UP or i.direction == DIRECTION.DOWN:
            v.append(i)
    return v, h


def hasIntersection(sV, sH):
    segHor_src_x = sH.pA.x if sH.pA.x < sH.pB.x else sH.pB.x
    segHor_dst_x = sH.pB.x if sH.pA.x < sH.pB.x else sH.pA.x
    segVer_src_y = sV.pA.y if sV.pA.y < sV.pB.y else sV.pB.y
    segVer_dst_y = sV.pB.y if sV.pA.y < sV.pB.y else sV.pA.y
    return segHor_src_x < sV.pA.x < segHor_dst_x and segVer_src_y < sH.pA.y < segVer_dst_y

def getClosestIntersection(wire0, wire1):

    V0, H0 = filterByDirection(wire0)
    V1, H1 = filterByDirection(wire1)
    
    manhattanDistances = []

    for v0 in V0:
        for h1 in H1:
            if hasIntersection(v0, h1):
                manhattanDistances.append(abs(v0.pA.x) + abs(h1.pA.y))
    for v1 in V1:
        for h0 in H0:
            if hasIntersection(v1, h0):
                manhattanDistances.append(abs(v1.pA.x) + abs(h0.pA.y))

    manhattanDistances.sort()
    return manhattanDistances[0]


def createWire(centralPort, inputWire):
    inputWire = convertToArray(inputWire)
    wire = []
    pointSrc = centralPort
    for input in inputWire:
        segment = calculateSegment(pointSrc, input)
        wire.append(segment)
        pointSrc = segment.pB
    return wire


def main(filename):
    input = open(filename, 'r').readlines()
    inputWire0 = input[0].strip('\n')
    inputWire1 = input[1].strip('\n')

    centralPort = Point(0, 0)
    wire0 = createWire(centralPort, inputWire0)
    wire1 = createWire(centralPort, inputWire1)

    result = getClosestIntersection(wire0, wire1)
    print("Solution: {Result}".format(Result=result))

# testing
IntersectTest(WireSegment(Point(6, 7), Point(6, 3), None, None), WireSegment(Point(3, 5), Point(8, 5), None, None), True)
IntersectTest(WireSegment(Point(6, 7), Point(6, 3), None, None), WireSegment(Point(8, 5), Point(3, 5), None, None), True)
IntersectTest(WireSegment(Point(0, 0), Point(0, 7), None, None), WireSegment(Point(8, 5), Point(3, 5), None, None), False)
IntersectTest(WireSegment(Point(6, 7), Point(6, 3), None, None), WireSegment(Point(0, 0), Point(8, 0), None, None), False)
IntersectTest(WireSegment(Point(3, 5), Point(3, 2), None, None), WireSegment(Point(6, 3), Point(2, 3), None, None), True)
CompleteTest("R8,U5,L5,D3", "U7,R6,D4,L4", 6)
CompleteTest("R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83", 159)
CompleteTest("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7", 135)

# program
main("input.in")







