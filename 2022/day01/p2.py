
def CalculateTotalCaloriesFromTopThree(caloriesList):
    elfArray = [0]
    for kcal in caloriesList:
        if (kcal == "\n"):
            elfArray.append(0)
        else:
            elfArray[-1] += int(kcal)

    elfArray.sort()

    return elfArray[-1] + elfArray[-2] + elfArray[-3]

def main(filename):
    input = open(filename, 'r')
    lines = input.readlines()
    totalCalories = CalculateTotalCaloriesFromTopThree(lines)
    print("Solution: {totalCalories}".format(totalCalories=totalCalories))

# Program
main('input.in')
