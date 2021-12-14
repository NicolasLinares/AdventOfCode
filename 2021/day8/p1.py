

def test1_CheckNumberOfDigits(filename, expected):
    input = open(filename, 'r').readlines()
    input = GetRightPart(input)
    result = GetNumberOfDigits(input)
    assert(result == expected)

def GetRightPart(input):
    for i in range(len(input)):
        input[i] = input[i].split(' | ')[1].strip()
    return input

def GetNumberOfDigits(input):
    total = 0
    for segments in input:
        segments = segments.split(' ')
        for segment in segments:
            length = len(segment)
            if (length == 2 or length == 3 or length == 4 or length == 7):
                total += 1
    return total

def main(filename):
    input = open(filename, 'r').readlines()
    input = GetRightPart(input)
    total = GetNumberOfDigits(input)
    print("Solution: {total}".format(total=total))

# testing
test1_CheckNumberOfDigits('test.in', 26)

# program
main("input.in")