import re

def test1_CheckNumberOfPaths(filename, expected):
    input = open(filename, 'r').readlines()
    result = CalculateNumberOfPaths(input)
    assert(result == expected)

START_CAVE = 'start'
END_CAVE = 'end'

class SubterraneanSubsystem:

    def __init__(self):
        self.map = dict()
        self.counter = 0

    def AddPath(self, path):
        src, dst = path[0], path[1]
        if src not in self.map:
            self.map[src] = []
        if dst not in self.map:
            self.map[dst] = []
        self.map[src].append(dst)
        self.map[dst].append(src)
        # print(self.map)

    def IsStartOrEndCave(self, cave):
        return cave == START_CAVE or cave == END_CAVE

    def IsSmallCave(self, cave):
        return bool(re.match("[a-z]", cave))

    def FindPaths(self):
        visited = dict()
        for cave in self.map:
            visited[cave] = False if self.IsStartOrEndCave(cave) or self.IsSmallCave(cave) else 0
        self.VisitePaths(START_CAVE, END_CAVE, visited)
        return self.counter

    def IsVisited(self, cave, visited):
        if self.IsStartOrEndCave(cave) or self.IsSmallCave(cave):
            return visited[cave]
        return False
            
    def VisitePaths(self, s, d, visited):
        visited[s] = True if self.IsStartOrEndCave(s) or self.IsSmallCave(s) else visited[s] + 1
        if s == d:
            self.counter += 1
        else:
            i = 0
            while i < len(self.map[s]):
                cave = self.map[s][i]
                if not self.IsVisited(cave, visited):
                    self.VisitePaths(cave, d, visited)
                i += 1

        visited[s] = False if self.IsStartOrEndCave(s) or self.IsSmallCave(s) else visited[s] - 1

def CalculateNumberOfPaths(input):
    Map = SubterraneanSubsystem()
    for line in input:
        path = line.strip().split('-')
        Map.AddPath(path)
    
    total = Map.FindPaths()
    return total

def main(filename):
    input = open(filename, 'r').readlines()
    total = CalculateNumberOfPaths(input)
    print("Solution: {total}".format(total=total))

# testing
test1_CheckNumberOfPaths('test1.in', 10)
test1_CheckNumberOfPaths('test2.in', 19)
test1_CheckNumberOfPaths('test3.in', 226)

# program
main("input.in")