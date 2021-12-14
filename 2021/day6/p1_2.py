
def test1_GetCorrectNumberOfLanternFish(input, maxDays, expected):
    result = GetNumberOfLanternfish(input, maxDays)
    assert(result == expected)

RESET_FISH_TIMER = 6
NEW_FISH_TIMER = 8

def GetNumberOfLanternfish(input, maxDays):
    counter = [0]*(NEW_FISH_TIMER+1)

    for i in input:
        counter[i] += 1

    for day in range(1, maxDays + 1):
        number_of_rotations = 2
        rotated = counter[number_of_rotations-1:] + [counter[0]]
        rotated[RESET_FISH_TIMER] = rotated[RESET_FISH_TIMER] + counter[0]
        counter = rotated

    return sum(counter)

def main(filename, days):
    input = open(filename, 'r').read().split(',')
    input = [int(d) for d in input]
    total = GetNumberOfLanternfish(input, days)
    print("After {day} days: {total}".format(day=days, total=total))

# testing

test1_GetCorrectNumberOfLanternFish([3,4,3,1,2], 18, 26)
test1_GetCorrectNumberOfLanternFish([3,4,3,1,2], 80, 5934)
test1_GetCorrectNumberOfLanternFish([3,4,3,1,2], 256, 26984457539)

# program
main("input.in", 80)
main("input.in", 256)