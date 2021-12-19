
def test1_CheckSyntaxError(filename, expected):
    input = open(filename, 'r').readlines()
    result = CalculateSyntaxError(input)
    assert(result == expected)

OPEN_CHARS = ['{', '[', '(', '<']
CLOSE_CHARS = ['}', ']', ')', '>']
SCORE_TABLE = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

def IsClose(character):
    return character in CLOSE_CHARS

def IsCouple(openChar, closeChar):
    return OPEN_CHARS.index(openChar) == CLOSE_CHARS.index(closeChar)

def CalculateScore(stack):
    total = 0
    while len(stack) > 0:
        character = stack.pop()
        total = total*5 + SCORE_TABLE[character]
    return total

def GetMiddleScore(totalScores):
    middleIndex = int((len(totalScores) - 1)/2)
    totalScores = sorted(totalScores)
    return totalScores[middleIndex]

def IsIncompleteLine(stack):
    return len(stack) > 0

def CalculateSyntaxError(input):
    totalScores = []
    for line in input:
        line = line.strip()
        stack = []
        for character in line:
            if IsClose(character):
                openChar = stack.pop()
                if not IsCouple(openChar, character):
                    # discard the corrupted lines
                    stack = []
                    break
            else:
                stack.append(character)

        if IsIncompleteLine(stack):
            total = CalculateScore(stack)
            totalScores.append(total)
    
    return GetMiddleScore(totalScores)


def main(filename):
    input = open(filename, 'r').readlines()
    total = CalculateSyntaxError(input)
    print("Solution: {total}".format(total=total))

# testing
test1_CheckSyntaxError('test.in', 288957)

# program
main("input.in")