import math


def test(inputMass, expectedMass):
    result = CalculateTotalMass(inputMass)
    assert(result == expectedMass)

def CalculateTotalMass(mass):
    totalMass = math.floor(mass/3)-2
    if (totalMass <= 0):
        return 0
    return totalMass + CalculateTotalMass(totalMass)

def main(filename):
    input = open(filename, 'r')
    lines = input.readlines()
    total = 0
    for mass in lines:
        mass = int(mass)
        total += CalculateTotalMass(mass)

    total = int(total)
    print("Solution: {totalMass}".format(totalMass=total))

# testing
test(12, 2)
test(14, 2)
test(1969, 966)
test(100756, 50346)

# Program
main("input.in")
