import re

def GetBingoBoards(lines):
    boards = []
    board = []
    i = 0
    for line in lines:
        if (i == 5):
            i = 0
            boards.append(board)
            board = []
        
        line = re.split('\s+', line.strip())
        if(len(line) != 1):
            boardRow = list(map(int, line))
            board.append(boardRow)
            i += 1

    return boards

def GetBingoSubsystemList(firstLine):
    return list(map(int, firstLine.strip('\n').split(',')))

def MarkNumberIfExists(board, number):
    for i, row in enumerate(board):
        for j, num in enumerate(row):
            if(num == number):
                board[i][j] = -1
    return board

def CheckBingo(board):

    def CheckHorizontal(board):
        i = 0
        bingo = False
        while (i < len(board)):
            j = 0
            while (j < len(board)):
                num = board[i][j]
                if num != -1:
                    break
                j += 1
            if (j == len(board)):
                bingo = True
                break
            i += 1
        return bingo

    def CheckVertical(board):
        j = 0
        bingo = False
        while (j < len(board)):
            i = 0
            while (i < len(board)):
                num = board[i][j]
                if num != -1:
                    break
                i += 1
            if (i == len(board)):
                bingo = True
                break
            j += 1
        return bingo

    return CheckVertical(board) or CheckHorizontal(board)

def SumUnmarkedNumbers(board):
    total = 0
    for row in board:
        for num in row:
            if(num != -1):
                total += num
    return total

def PlayBingo(bingoSubsystem, boards):
    for number in bingoSubsystem:
        for i, board in enumerate(boards):
            boards[i] = MarkNumberIfExists(board, number)
            isBingo = CheckBingo(boards[i])
            if isBingo:
                total = SumUnmarkedNumbers(boards[i])
                return total * number
    return None

def main(filename):
    input = open(filename, 'r')
    lines = input.readlines()

    bingoSubsystem = GetBingoSubsystemList(lines[0])
    boards = GetBingoBoards(lines[1:])
    total = PlayBingo(bingoSubsystem, boards)
    print("Solution: {total}".format(total=total))

# Program
main('input.in')
