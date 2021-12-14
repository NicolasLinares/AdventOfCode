
from typing import Match

def test(input, expected):
    result = CalculatePowerConsumption(input)
    assert(result == expected)

class BIT:
    ZERO = '0'
    ONE = '1'

def InitializeBitsCounter(length):
    return [dict.fromkeys([BIT.ZERO,BIT.ONE], 0) for x in range(length)]

def GetGammaEpsilonRatesInDec(counter):
    gammaRateBin = ''
    epsilonRateBin = ''
    for bit in counter:
        if bit[BIT.ZERO] < bit[BIT.ONE]:
            gammaRateBin += BIT.ONE
            epsilonRateBin += BIT.ZERO
        else:
            gammaRateBin += BIT.ZERO
            epsilonRateBin += BIT.ONE

    gammaRateDec = int(gammaRateBin, 2) 
    epsilonRateDec = int(epsilonRateBin, 2)   

    return (gammaRateDec, epsilonRateDec)

def CalculatePowerConsumption(diagnosticReport):
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
    
    (gammaRateDec, epsilonRateDec) = GetGammaEpsilonRatesInDec(counter)
    return gammaRateDec * epsilonRateDec

def main(filename):
    input = open(filename, 'r')
    lines = input.readlines()
    total = CalculatePowerConsumption(lines)
    print("Solution: {total}".format(total=total))

# testing
test(['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010'], 198)

# Program
main('input.in')
