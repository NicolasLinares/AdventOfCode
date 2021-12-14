
NUMBER_EXPECTED = 19690720

class OPERATION:
    ADD = 1
    MULTIPLY = 2
    FINISH = 99

def test(inputData, expectedData):
    inputData = convertToIntArray(inputData)
    expectedData = convertToIntArray(expectedData)
    result = runIntcode(inputData)
    assert(result == expectedData)


def convertToIntArray(input):
    return map(int, input.split(","))

def runIntcode(input):
    i=0
    while input[i] != OPERATION.FINISH:
        positionA = input[i+1]
        positionB = input[i+2]
        dst = input[i+3]
        if input[i] == OPERATION.ADD:
            input[dst] = input[positionA] + input[positionB]
        elif input[i] == OPERATION.MULTIPLY:
            input[dst] = input[positionA] * input[positionB]
        i += 4
    return input

def preprocess(input, noun, verb):
    input[1] = noun
    input[2] = verb
    return input

def findNounAndVerb(data):
    backup = data[:]
    for noun in range(0,99):
        for verb in range(0,99):
            data = preprocess(data, noun, verb)
            processedData = runIntcode(data)
            result = processedData[0]
            if (result == NUMBER_EXPECTED):
                return (noun, verb)
            data = backup[:]
    return None

def main(filename):
    input = open(filename, 'r').read()
    data = convertToIntArray(input)
    (noun, verb) = findNounAndVerb(data)
    result = 100*noun+verb
    print("Solution: {Result}".format(Result=result))

# testing
# test("1,0,0,0,99", "2,0,0,0,99")
# test("2,3,0,3,99", "2,3,0,6,99")
# test("2,4,4,5,99,0", "2,4,4,5,99,9801")
# test("1,1,1,4,99,5,6,0,99", "30,1,1,4,2,5,6,0,99")

# program
main("input.in")