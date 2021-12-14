

def test(n, expectedData):
    result = isAscending(n) and atLeastTwoAdjacents(str(n))
    assert(result == expectedData)

def atLeastTwoAdjacents(n):
    repeat_count = 0
    for n1, n2 in zip(n, n[1:]):
        if n1 == n2:
            repeat_count += 1
        else:
            if repeat_count == 1:
                return True
            repeat_count = 0
    return repeat_count == 1

def isAscending(n):
    return "".join(sorted(str(n))) == str(n)

def getNumberOfPassword(a, b):
    count = 0
    for n in range(a + 1, b):
        if (isAscending(n) and atLeastTwoAdjacents(str(n))):
            count += 1
    return count


def main():

    a = 367479
    b = 893698
    result = getNumberOfPassword(a, b)
    print("Solution: {Result}".format(Result=result))

# testing
test(367479, False)
test(111111, False)
test(223450, False)
test(123789, False)
test(112233, True)
test(123444, False)
test(111122, True)

# program
main()




