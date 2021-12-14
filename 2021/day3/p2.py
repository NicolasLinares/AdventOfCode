from typing import Match

def test1_CorrectOxygenValue(input, expected):
    result = GetRating(input, BIT.ZERO, BIT.ONE)
    assert(result == expected)

def test2_CorrectCO2Value(input, expected):
    result = GetRating(input, BIT.ONE, BIT.ZERO)
    assert(result == expected)

def test3_CorrectLifeSupportRating(input, expected):
    result = CalculateLifeSupportRating(input)
    assert(result == expected)


class BIT:
    ZERO = '0'
    ONE = '1'

def GetRating (diagnosticReport, bit1, bit2):

    def GetSubsetRating(subset, value, index):
        result = []
        for bits in subset:
            if (bits[index] == value):
                result.append(bits)
        return result

    def InitializeBitsCounter(length):
        return [dict.fromkeys([BIT.ZERO,BIT.ONE], 0) for x in range(length)]

    def GetNumberBitsInEachPosition(diagnosticReport):
        numBitsInReport = len(diagnosticReport[0].strip('\n'))
        counter = InitializeBitsCounter(numBitsInReport)
        for bits in diagnosticReport:
            i = 0
            for bit in bits:
                match (bit):
                    case BIT.ZERO:
                        counter[i][BIT.ZERO] += 1 
                    case BIT.ONE:
                        counter[i][BIT.ONE] += 1 
                i += 1
        
        return counter

    def IsNotFound (list):
        return len(list) > 1

    subList = diagnosticReport
    i = 0
    while (IsNotFound(subList)):
        counter = GetNumberBitsInEachPosition(subList)
        bitToKeep = bit1
        if counter[i][BIT.ZERO] <= counter[i][BIT.ONE]:
            bitToKeep = bit2
        subList = GetSubsetRating(subList, bitToKeep, i)
        i += 1

    return subList[0]

def GetOxygenRating(diagnosticReport):
    mostCommonBitToKeep = BIT.ZERO
    equalBitToKeep = BIT.ONE
    return GetRating(diagnosticReport, mostCommonBitToKeep, equalBitToKeep)

def GetCO2Rating(diagnosticReport):
    leastCommonBitToKeep = BIT.ONE
    equalBitToKeep = BIT.ZERO
    return GetRating(diagnosticReport, leastCommonBitToKeep, equalBitToKeep)

def CalculateLifeSupportRating(diagnosticReport):
    oxigenRateBin = GetOxygenRating(diagnosticReport)
    co2RateBin = GetCO2Rating(diagnosticReport)
    oxigenRateDec = int(oxigenRateBin, 2)
    co2RateDec = int(co2RateBin, 2)
    return oxigenRateDec * co2RateDec

def main(filename):
    input = open(filename, 'r')
    lines = input.readlines()
    total = CalculateLifeSupportRating(lines)
    print("Solution: {total}".format(total=total))

# testing
inputTest = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
test1_CorrectOxygenValue(inputTest, '10111')
test2_CorrectCO2Value(inputTest, '01010')
test3_CorrectLifeSupportRating(inputTest, 230)

# Program
main('input.in')