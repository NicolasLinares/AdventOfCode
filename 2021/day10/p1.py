

def test1_CheckSyntaxError(filename, expected):
    input = open(filename, 'r').readlines()
    result = CalculateSyntaxError(input)
    assert(result == expected)

OPEN_CHARS = ['{', '[', '(', '<']
CLOSE_CHARS = ['}', ']', ')', '>']
SCORE_TABLE = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

def IsClose(character):
    return character in CLOSE_CHARS

def IsCouple(openChar, closeChar):
    return OPEN_CHARS.index(openChar) == CLOSE_CHARS.index(closeChar)

def CalculateSyntaxError(input):
    total = 0
    for line in input:
        line = line.strip()
        stack = []
        for character in line:
            if IsClose(character):
                openChar = stack.pop()
                if not IsCouple(openChar, character):
                    total += SCORE_TABLE[character]
                    break
            else:
                stack.append(character)

    return total

def main(filename):
    input = open(filename, 'r').readlines()
    total = CalculateSyntaxError(input)
    print("Solution: {total}".format(total=total))

# testing
test1_CheckSyntaxError('test.in', 26397)

# program
main("input.in")