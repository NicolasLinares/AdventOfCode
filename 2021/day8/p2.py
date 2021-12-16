
def test1_CheckNumberOfDigits(filename, expected):
    input = open(filename, 'r').readlines()
    result = ParsePatterns(input)
    assert(result == expected)

def GetPatterns(input):
    input = input.split(' | ')
    left = input[0].strip().split(' ')
    right = input[1].strip().split(' ')
    return (left, right)

def GetEasyPattern(length, leftPatterns):
    for pattern in leftPatterns:
        if len(pattern) == length:
            return pattern

def ContainsPattern(pattern, segment):
    for letter in pattern:
        if letter not in segment:
            return False
    return True

def GetNumberOfNotMatching(pattern, segment):
    notMatch = 0
    for letter in pattern:
        if letter not in segment:
            notMatch += 1
    return notMatch

_1_LENGTH_PATTERN = 2
_4_LENGTH_PATTERN = 4
_7_LENGTH_PATTERN = 3
_8_LENGTH_PATTERN = 7

def TryParseToEasyDigit(segment):
    length = len(segment)
    if length == _1_LENGTH_PATTERN:
        return 1
    if length == _4_LENGTH_PATTERN:
        return 4
    if length == _7_LENGTH_PATTERN:
        return 7
    if length == _8_LENGTH_PATTERN:
        return 8
    return None

def IsNotEasyDigit(digit):
    return digit == None

def IsZero(segment, fourPattern, possibleSegment):
    return not ContainsPattern(fourPattern, possibleSegment) and ContainsPattern(segment, possibleSegment)

def IsTwo(segment, fourPattern, possibleSegment):
    return GetNumberOfNotMatching(fourPattern, possibleSegment) == 2 and ContainsPattern(segment, possibleSegment)

def IsThree(segment, onePattern, possibleSegment):
    return ContainsPattern(onePattern, possibleSegment) and ContainsPattern(segment, possibleSegment)

def IsFive(segment, fourPattern, possibleSegment):
    return GetNumberOfNotMatching(fourPattern, possibleSegment) == 1 and ContainsPattern(segment, possibleSegment)

def IsSix(segment, onePattern, possibleSegment):
    return not ContainsPattern(onePattern, possibleSegment) and ContainsPattern(segment, possibleSegment)

def IsNine(segment, fourPattern, possibleSegment):
    return ContainsPattern(fourPattern, possibleSegment) and ContainsPattern(segment, possibleSegment)


def ParseToComplexDigit(segment, leftPatterns):
    segmentLength = len(segment)
    possibleSegmentsMatches = [pattern for pattern in leftPatterns if len(pattern) == segmentLength]
    onePattern = GetEasyPattern(_1_LENGTH_PATTERN, leftPatterns)
    fourPattern = GetEasyPattern(_4_LENGTH_PATTERN, leftPatterns)

    for possibleSegment in possibleSegmentsMatches:
        if segmentLength == 5:
            if IsThree(segment, onePattern, possibleSegment):
                return 3
            if IsFive(segment, fourPattern, possibleSegment):
                return 5
            if IsTwo(segment, fourPattern, possibleSegment):
                return 2
        if segmentLength == 6:
            if IsSix(segment, onePattern, possibleSegment):
                return 6
            if IsNine(segment, fourPattern, possibleSegment):
                return 9
            if IsZero(segment, fourPattern, possibleSegment):
                return 0
    return None


def ParseRigthPatternsToNumber(leftPatterns, rigthPatterns):
    finalNumber = ''
    for segment in rigthPatterns:
        digit = TryParseToEasyDigit(segment)
        if IsNotEasyDigit(digit):
            digit = ParseToComplexDigit(segment, leftPatterns)
        finalNumber += str(digit)
    return int(finalNumber)

def ParsePatterns(input):
    total = 0
    for line in input:
        (leftPatterns, rigthPatterns) = GetPatterns(line)
        finalNumber = ParseRigthPatternsToNumber(leftPatterns, rigthPatterns)
        total += finalNumber
    return total

def main(filename):
    input = open(filename, 'r').readlines()
    total = ParsePatterns(input)
    print("Solution: {total}".format(total=total))

# testing
test1_CheckNumberOfDigits('test.in', 61229)

# program
main("input.in")



# Estrategia:
#------------------------------------------------------------------------------------
# Partiendo de 4 dígitos conocidos (easy digits), podemos sacar el resto:
#     - Formado por 5 letras:
#         - Dígito 3: incluye el patrón del 1
#         - Dígito 5: Si del 4 sobra una letra, entonces es un 5
#         - Dígito 2: si del 4 sobran 2 letras, es un 2
#     - Formado por 6 letras:
#         - Dígito 6: no incluye el patrón del 1, los dos siguientes sí
#         - Dígito 9: incluye el patrón del 1 y el del 4
#         - Dígito 0: incluye el patrón del 1 y NO el del 4
