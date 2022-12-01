
def CalculateTotalCalories(caloriesList):
    elfIndex = 0
    elfArray = [0]
    for kcal in caloriesList:
        if (kcal == "\n"):
            lastElf = elfArray[-1]
            mostCaloriesElf = elfArray[elfIndex]
            elfIndex = elfIndex if mostCaloriesElf > lastElf else len(elfArray) - 1
            elfArray.append(0)
        else:
            elfArray[-1] += int(kcal)

    return elfArray[elfIndex]

def main(filename):
    input = open(filename, 'r')
    lines = input.readlines()
    totalCalories = CalculateTotalCalories(lines)
    print("Solution: {totalCalories}".format(totalCalories=totalCalories))

# Program
main('input.in')
