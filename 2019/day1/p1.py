import math

def main(filename):
    input = open(filename, 'r')
    lines = input.readlines()
    total = 0
    for mass in lines:
        mass = int(mass)
        total += math.floor(mass/3)-2

    total = int(total)
    print("Solution: {totalMass}".format(totalMass=total))


main("input.in")