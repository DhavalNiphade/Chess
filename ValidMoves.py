def isValidPawn(board,newPos,currPos,dist,nextPos):
    # Check if next movable block is a 0 and within the bounds of the board
    if newPos < 63 and newPos > 0 and board[newPos] == 0 :   # Bounds the board and finds an empty space to move to
        return True
    return False

def isValidKnight(board,newPos,currPos,dist,nextPos):

    if board[currPos]>0:
        a = (newPos < 63 and newPos > 0 and (board[newPos] == 0 or board[newPos] < 0))
    else:
        a = (newPos < 63 and newPos > 0 and (board[newPos] == 0 or board[newPos] > 0))

    b = dist==3    # Check if the move is 3 manhattan units only

    if(a and b):
        return True
    return False

def isValidBishop(board,newPos,currPos,dist,nextPos):

    b = dist%2==0  # Check if manhattan distance is divisible by 2

    # Capture or empty move
    if(board[currPos] > 0):
        if newPos <  63 and newPos > 0 and (board[newPos] == 0 or board[newPos]<0) and b:
            return True
    elif(board[currPos] < 0):
        if newPos < 63 and newPos > 0 and (board[newPos] == 0 or board[newPos]>0) and b :
            return True
    return False

def isValidRook(board,newPos,currPos,dist,nextPos):

    # Move to blank position or capture an enemy piece
    if(board[currPos]>0):
        if newPos < 63 and newPos > 0 and (board[newPos] == 0 or board[newPos]<0):
            return True
    elif(board[currPos]<0):
        if newPos < 63 and newPos > 0 and (board[newPos] == 0 or board[newPos]>0):
            return True
    return False

def isValidQueen(board,newPos,currPos,dist,nextPos):
    # return isValidRook(board,newPos,currPos,dist) and isValidBishop(board,newPos,currPos,dist)
    # Move to blank position or capture an enemy piece

    b = dist % 2 == 0  # Check if manhattan distance is divisible by 2 - for bishop

    if(board[currPos]>0):
        if(nextPos in [(1,1),(1,-1),(-1,1),(-1,-1)]):
            if newPos < 63 and newPos > 0 and (board[newPos] == 0 or board[newPos]<0) and b:
                return True
        else:
            if newPos < 63 and newPos > 0 and (board[newPos] == 0 or board[newPos]<0):
                return True

    elif(board[currPos]<0):
        if (nextPos in [(1, 1), (1, -1), (-1, 1), (-1, -1)]):
            if newPos < 63 and newPos > 0 and (board[newPos] == 0 or board[newPos]>0) and b:
                return True
        else:
            if newPos < 63 and newPos > 0 and (board[newPos] == 0 or board[newPos]>0):
                return True
    return False

def isValidKing(board,newPos,currPos,dist,nextPos):
    if(board[currPos]>0):
        if newPos < 63 and newPos > 0 and (board[newPos] == 0 or board[newPos]<0):
            return True
    elif(board[currPos]<0):
        if newPos < 63 and newPos > 0 and (board[newPos] == 0 or board[newPos]>0):
            return True
    return False


# ----------------------------------------------------------------------------------------------------------------- #

def canPawnCapture(board,newPos,currPos):
    if(board[currPos] > 0):  # White is playing
        if newPos < 63 and newPos > 0 and board[newPos]<0:
            return True

    if (board[currPos] < 0):  # Black is playing
        if newPos < 63 and newPos > 0 and  board[newPos]>0:
            return True
    return False


# Defines the corresponding moves for the piece that is already there
legalMovesFunctionMapper = {
                            1 : isValidPawn,
                            3 : isValidKnight,
                            4 : isValidBishop,
                            5 : isValidRook,
                            9 : isValidQueen,
                            200 : isValidKing
}


