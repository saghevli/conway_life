# conway's game of life?
# rules:
# any live cell with fewer than two live neighbors dies
# a live cell with two or three live neighbors lives
# a live cell with four or more live neighbors dies
# a dead cell with > 3 live neighbors

import time

BOARD_SIZE = 41
generation = 0

def main():
    interval = .5
    board = [[0 for i in range(BOARD_SIZE)] for i in range(BOARD_SIZE)]
    print "input comma separated inital state coordinates  with \"end\" on the last line"
    input = raw_input()
    while input != "end" :
        coordinates = [int(i) for i in input.split(',')]
        print coordinates
        print str(coordinates[0]) + "|" + str(coordinates[1])
        board[coordinates[0]][coordinates[1]] = 1
        input = raw_input()
    user_interval = raw_input("generation interval in seconds? default is .5, enter 'n' for default: ")
    if user_interval != "n":
        interval = float(user_interval)

    animate(board, interval)
    
def animate(board, interval):
    while True:
        printBoard(board)
        board = update(board)
        time.sleep(interval)

def update(board):
    global generation
    generation += 1
    newBoard = [[0 for i in range(BOARD_SIZE)] for i in range(BOARD_SIZE)]
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            liveNeighbors = numberLiveNeighbors(board, i, j)
            # if alive and 3 or 3 live neighbors, stay alive
            if board[i][j] and (liveNeighbors == 2 or liveNeighbors == 3) :
                newBoard[i][j] = 1
            if ~board[i][j] and liveNeighbors == 3 :
                newBoard[i][j] = 1

    return newBoard


def numberLiveNeighbors(board, i, j):
    if i >= BOARD_SIZE or j >= BOARD_SIZE or i < 0 or j < 0:
        return -1;
    numLiveNeighbors = 0;
    numLiveNeighbors += isLive(board, i - 1, j - 1); # up, left
    numLiveNeighbors += isLive(board, i - 1, j); # up
    numLiveNeighbors += isLive(board, i - 1, j + 1); # up, right
    numLiveNeighbors += isLive(board, i, j - 1); # left
    numLiveNeighbors += isLive(board, i, j + 1); # right
    numLiveNeighbors += isLive(board, i + 1, j - 1); # down, left
    numLiveNeighbors += isLive(board, i + 1, j); # down
    numLiveNeighbors += isLive(board, i + 1, j + 1); # down, right
    return numLiveNeighbors

# if out of bounds, not alive. if in bounds, check. 1 indicates alive, 0 dead
def isLive(board, i, j):
    if i >= BOARD_SIZE or j >= BOARD_SIZE or i < 0 or j < 0:
        return 0
    return board[i][j]

def printBoard(board):
    print "************************* Generation " + str(generation) + " *************************"
    for i in range(BOARD_SIZE):
        line = ""
        for j in range(BOARD_SIZE):
            if board[i][j] :
                line += "& "
            else :
                line += "_ "
        print line

if __name__ == "__main__":
    main()
