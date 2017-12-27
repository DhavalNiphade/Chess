def nextMove(board,pos,turn):
    moveList = []
    if turn == 'w':
        if board[pos]==1:
            if board[pos+8]>0 and board[pos+8+1]>0:
                return None
            board[pos]=0
            board[pos+8]=1

    return moveList

    print2D(board)



def Immovable(board,currPos,turn):
    # Check all possible avenues to move within
    if board[currPos] in [3,-3]:
        return False

    oldRow,oldCol = int(currPos/8) , int(currPos%8)

    a,b,c,d = True,True,True,True

    if currPos==0 : # Check if its a corner position
        if board[currPos+1] > 0 and board[currPos+8] > 0:
            return True

    if currPos==63 : # Check if its a corner position
        if board[currPos-1] > 0 and board[currPos-8] > 0:
            return True

    if currPos==7 : # Check if its a corner position
        if board[currPos-1] > 0 and board[currPos+8] > 0:
            return True

    if currPos==56 : # Check if its a corner position
        if board[currPos+1] > 0 and board[currPos-8] > 0:
            return True

    if oldRow==0:
        if board[currPos+1] > 0 and board[currPos-1] > 0 and board[currPos+8] > 8:
            return True

    if oldRow==7:
        if board[currPos+1] > 0 and board[currPos-1] > 0 and board[currPos-8] > 8:
            return True

