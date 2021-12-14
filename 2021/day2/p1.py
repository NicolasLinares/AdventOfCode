from typing import Match

def test(input, expected):
    result = CalculatePosition(input)
    assert(result == expected)


class COMMAND:
    FORWARD = 'forward'
    UP = 'up'
    DOWN = 'down'

def CalculatePosition(commands):

    horizontal = 0
    depth = 0
    for command in commands:
        command = command.split(' ')
        move = command[0]
        units = int(command[1])

        match (move):
            case COMMAND.FORWARD:
                horizontal += units
            case COMMAND.UP:
                depth -= units
            case COMMAND.DOWN:
                depth += units

    return horizontal * depth

def main(filename):
    input = open(filename, 'r')
    lines = input.readlines()
    total = CalculatePosition(lines)
    print("Solution: {total}".format(total=total))

# testing
test(['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2'], 150)

# Program
main('input.in')
