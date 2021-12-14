

def test(n, expectedData):
    result = satisfyFacts(n)
    assert(result == expectedData)


def satisfyFacts(n):
    i = 0
    n = str(n)
    l = len(n)
    atLeastTwoAdjacent = 0
    while(i < l - 1):
        current = int(n[i])
        next = int(n[i+1])
        if (next < current):
            return False
        if (current == next):
            atLeastTwoAdjacent += 1
        i += 1

    return atLeastTwoAdjacent > 0

def getNumberOfPassword(a, b):
    count = 0
    for n in range(a + 1, b):
        if (satisfyFacts(n)):
            count += 1
        
    return count


def main():

    a = 367479
    b = 893698
    result = getNumberOfPassword(a, b)
    print("Solution: {Result}".format(Result=result))

# testing
test(367479, False)
test(111111, True)
test(223450, False)
test(123789, False)

# program
main()








