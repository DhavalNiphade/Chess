    #!usr/bin/env python3

# Author : Dhaval R Niphade
# Class : CSCI B 551 Elements of Artificial Intelligence
# Prof. : Dr. David Crandall
# Date of Creation : October 17, 2017
# Last Modified : October 21, 2017

# IMPORT SECTION
import sys
from copy import deepcopy
import Vars
import ValidMoves

# maxVal = int(float("inf"))
# minVal = int(float("-inf"))
#
# print(maxVal)
# print(minVal)


# ----------------------------------------------------------------------------------------------------------------------

# SECTION 1 : MOVE GENERATORS
# Generate white moves
def generateWhiteMoves(board, currPos):
    movesList = []
    capFlag = False

    if currPos > 63 or currPos < 0 or board[currPos]==0 or board[currPos]<0:
        # print("Checkpoint A")
        return movesList    # Return an empty list

    for nextPos in Vars.moveIndex[board[currPos]][0]:   # For each possible move within the board for a given piece at a given position
        # print("Checkpoint B")

        for tiles in range(1,Vars.moveIndex[board[currPos]][1]):
            # print("Checkpoint C")

            # Check the valid moves for the given piece
            oldRow, oldCol = int(currPos / 8), int(currPos % 8)
            # newRow, newCol = (oldRow + nextPos[0] * tiles), (oldCol + nextPos[1] * tiles)
            newPos = (oldRow + nextPos[0]*tiles) * 8 + (oldCol + nextPos[1]*tiles)  #Use tiles to determine the length to which we traverse
            newRow,newCol = int(newPos/8), int(newPos%8)

            dist = abs(newRow - oldRow) + abs(newCol - oldCol)
            # print(newPos,nextPos, newRow, newCol, dist)

            if (board[currPos]==1 or board[currPos]==-1):
                capturePositions = [(oldRow+1)*8 + (oldCol +1) , (oldRow+1)*8 + (oldRow-1)]
                for pos in capturePositions:
                    if ValidMoves.canPawnCapture(board,pos,currPos):
                        newBoard = deepcopy(board)
                        newBoard[currPos] = 0
                        newBoard[pos] = board[currPos]
                        movesList.append(newBoard)

            if ValidMoves.legalMovesFunctionMapper[abs(board[currPos])](board,newPos,currPos,dist,nextPos):

                if board[newPos]!=0:    # Capture condition
                    capFlag = True
                if nextPos in [(0,1),(0,-1)] and newRow != oldRow: #Row Overflow condition
                    break

                newBoard = deepcopy(board)
                newBoard[currPos]=0
                newBoard[newPos]=board[currPos]
                movesList.append(newBoard)
                if capFlag:
                    capFlag = False
                    break
            else:
                # print("Checkpoint D")
                break

    return movesList

# Generate black moves
def generateBlackMoves(board,currPos):
    movesList = []
    capFlag = False
    board = board[::-1]
    currPos = 63-currPos

    if(currPos > 63 or currPos < 0 or board[currPos]==0 or board[currPos]>0):
        # print("Checkpoint A")
        return movesList    # Return an empty list

    for nextPos in Vars.moveIndex[board[currPos]][0]:   # For each possible move within the board for a given piece at a given position
        # print("Checkpoint B")

        for tiles in range(1,Vars.moveIndex[board[currPos]][1]):
            # print("Checkpoint C")

            # Check the valid moves for the given piece
            oldRow, oldCol = int(currPos / 8), int(currPos % 8)
            # newRow, newCol = (oldRow + nextPos[0] * tiles), (oldCol + nextPos[1] * tiles)
            newPos = (oldRow + nextPos[0]*tiles) * 8 + (oldCol + nextPos[1]*tiles)  #Use tiles to determine the length to which we traverse
            newRow,newCol = int(newPos/8), int(newPos%8)

            dist = abs(newRow - oldRow) + abs(newCol - oldCol)
            # print(newPos,nextPos, newRow, newCol, dist)

            if (board[currPos]==1 or board[currPos]==-1):
                capturePositions = [(oldRow+1)*8 + (oldCol +1) , (oldRow+1)*8 + (oldRow-1)]
                for pos in capturePositions:
                    if ValidMoves.canPawnCapture(board,pos,currPos):
                        newBoard = deepcopy(board)
                        newBoard[currPos] = 0
                        newBoard[pos] = board[currPos]
                        movesList.append(newBoard)

            if ValidMoves.legalMovesFunctionMapper[abs(board[currPos])](board,newPos,currPos,dist,nextPos):

                if board[newPos]!=0:    # Capture condition
                    capFlag = True
                if nextPos in [(0,1),(0,-1)] and newRow != oldRow: #Row Overflow condition
                    break

                newBoard = deepcopy(board)
                newBoard[currPos]=0
                newBoard[newPos]=board[currPos]
                movesList.append(newBoard[::-1])
                if capFlag:
                    capFlag = False
                    break
            else:
                # print("Checkpoint D")
                break

    return movesList

# ----------------------------------------------------------------------------------------------------------------------

# SECTION 2 : EVALUATION FUNCTION
# Evaluation function
def computeEval(board,player):

    ''' Compute a N-part evaluation that computes an estimate of how much potential gain/loss is associated with the
        move.
        1. Materialistic gain = Sum up all the values of the board
        2. Mobility / Positional advantage
        3. Controls the centre position
    '''


    # 1. Materialistic gain - Who has more pieces
    retval=0
    retval+=sum(board)  # Sum up all the values of the board and get materialistic evaluation

    # 2. Check positional advantage
    if player == 'w':
        target = Vars.positionPreferenceMapper[board[pos]] # Find which favourableX list the current piece corresponds to and add the corresponding value
        retval += target[pos]
    if player == 'b':
        target = Vars.positionPreferenceMapper[board[pos]]  # Find which favourableX list the current piece corresponds to and add the corresponding value
        target = reversed(target)
        retval += target[pos]

    # 3. Controls center position
    if player == 'w':
        if board[27]>0 or board[28]>0 or board[35]>0 or board[36]>0:
            retval+=10

    if player == 'b':
        if board[27] < 0 or board[28] < 0 or board[35] < 0 or board[36] < 0:
            retval+=10

    return retval

# ----------------------------------------------------------------------------------------------------------------------

# HELPER FUNCTIONS AND DATA STRUCTURES
# Print as Linear board
def printAsBoard(board):
    print(''.join(Vars.valPiece[piece] for piece in board))


# Print board as a 2D matrix
'''Prints board as a 2D matrix'''
def print2D(board):
    print("\n".join(str(board[8*i:8*i+8]) for i in range(0,8)))

# Move Mapper
moveGenerator = {
    'w': generateWhiteMoves,
    'b': generateBlackMoves
}

moveSwapper = {
    'w' : 'b',
    'b' : 'w'
}

# ----------------------------------------------------------------------------------------------------------------------

# SECTION 2 : MINIMAX WITH ALPHA BETA PRUNING AND DEPTH CONTROL

horizon = 10
def abDecision(initialBoard,turn):

    allMoves = []
    for i in range(0, 64):
        temp = moveGenerator[turn](initialBoard, i)
        for moves in temp:
            allMoves.append(moves)


    for SPrime in allMoves:
        temp = MinValue(SPrime, (SPrime,float('-inf')), (SPrime,float('inf')),turn,0)
        retval = max((initialBoard,0),temp,key=lambda x : x[1])

    printAsBoard(retval[0])

def MaxValue(S,alpha,beta,turn,depth):

    # Terminating condition
    # for boards in S:
    if turn=='w':
        if -200 not in S:
            return (S,float('inf'))
        if 200 not in S:
            return (S,float('-inf'))
    else:
        if -200 not in S:
            return (S,float('-inf'))
        if 200 not in S:
            return (S,float('inf'))

    # Increment the depth for this level
    depth += 1

    # Second terminating condition
    global horizon
    if depth == horizon:
        return alpha

    # Successor function
    allMoves = []
    # for board in S:
    for i in range(0, 64):
        temp = moveGenerator[turn](S, i)
        for moves in temp:
            allMoves.append((moves,sum(moves))) # Create tuple of next board and its evaluation function

    # Pruning and maximizer
    for boards in allMoves:
        alpha = max(alpha,MinValue(boards[0],alpha,beta,turn,depth),key=lambda x : x[1])
        # print(alpha[1])
        if alpha[1] >= beta[1]:
            return alpha

    return alpha

def MinValue(S,alpha,beta,turn,depth):

    if turn=='b':
        if 200 not in S:
            return (S,float('-inf'))
        if -200 not in S:
            return (S,float('inf'))
    else:
        if 200 not in S:
            return (S,float('inf'))
        if -200 not in S:
            return (S,float('-inf'))

    # Increment depth for this level
    depth += 1

    # Second terminating condition
    global horizon
    if depth == horizon:
        return beta

    # Successor Function
    allMoves = []
    for i in range(0, 64):
        temp = moveGenerator[moveSwapper[turn]](S, i)
        for moves in temp:
            allMoves.append((moves, sum(moves)))  # Create tuple of next board and its evaluation function

    # Pruning and minimization
    for boards in allMoves:
        beta = min(beta,MaxValue(boards[0],alpha,beta,turn,depth),key=lambda x : x[1])
        if alpha[1] >= beta[1]:
            return beta
    return beta

# SECTION 0 : DRIVER AND MAIN FUNCTIONS
# Driver and Configuration
def main():

    # Accept input
    turn,initialBoard,timeLimit = sys.argv[1], sys.argv[2], sys.argv[3]
    board = [Vars.pieceVal[i] for i in initialBoard]

    # Test printing as a 2D board
    print(print2D(board))


    # someshit = generateMoves(board,26,'w')
    # print("\nResulting configurations")
    # for boardconfigs in someshit:
    #     print2D(boardconfigs)
    #     print("\n")

    printAsBoard(abDecision(board,turn))

if __name__ == '__main__':
    main()