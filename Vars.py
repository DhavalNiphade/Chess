# DEFINE PIECES AND MOVES SECTION

pieceVal = {'P':1 , 'p':-1, 'N':3 , 'n':-3 , 'B':4 , 'b':-4 , 'R':5, 'r':-5 , 'Q':9 , 'q':-9 , 'K':200 , 'k':-200 , '.':0}
valPiece = {1:'P' , -1:'p', 3:'N' , -3:'n' , 4:'B' , -4:'b' , 5:'R', -5:'r' , 9:'Q' , -9:'q' , 200:'K' , -200:'k' , 0:'.'}

favourablePawn = [0,  0,  0,  0,  0,  0,  0,  0,50, 50, 50, 50, 50, 50, 50, 50,10, 10, 20, 30, 30, 20, 10, 10,5,  5, 10, 25, 25, 10,  5,  5,0,  0,  0, 20, 20,  0,  0,  0,5, -5,-10,  0,  0,-10, -5,  5,5, 10, 10,-20,-20, 10, 10,  5, 0,  0,  0,  0,  0,  0,  0,  0]
favourableKnight = [-50,-40,-30,-30,-30,-30,-40,-50,-40,-20,  0,  0,  0,  0,-20,-40,-30,  0, 10, 15, 15, 10,  0,-30,-30,  5, 15, 20, 20, 15,  5,-30,-30,  0, 15, 20, 20, 15,  0,-30,-30,  5, 10, 15, 15, 10,  5,-30,-40,-20,  0,  5,  5,  0,-20,-40,-50,-40,-30,-30,-30,-30,-40,-50]
favourableBishop = [-20,-10,-10,-10,-10,-10,-10,-20,-10,  0,  0,  0,  0,  0,  0,-10,-10,  0,  5, 10, 10,  5,  0,-10,-10,  5,  5, 10, 10,  5,  5,-10,-10,  0, 10, 10, 10, 10,  0,-10,-10, 10, 10, 10, 10, 10, 10,-10,-10,  5,  0,  0,  0,  0,  5,-10,-20,-10,-10,-10,-10,-10,-10,-20]
favourableRook = [0,  0,  0,  0,  0,  0,  0,  0, 5, 10, 10, 10, 10, 10, 10,  5, -5,  0,  0,  0,  0,  0,  0, -5, -5,  0,  0,  0,  0,  0,  0, -5, -5,  0,  0,  0,  0,  0,  0, -5, -5,  0,  0,  0,  0,  0,  0, -5, -5,  0,  0,  0,  0,  0,  0, -5, 0,  0,  0,  5,  5,  0,  0,  0]
favourableQueen = [-20,-10,-10, -5, -5,-10,-10,-20, -10,  0,  0,  0,  0,  0,  0,-10, -10,  0,  5,  5,  5,  5,  0,-10, -5,  0,  5,  5,  5,  5,  0, -5, 0,  0,  5,  5,  5,  5,  0, -5, -10,  5,  5,  5,  5,  5,  0,-10, -10,  0,  5,  0,  0,  0,  0,-10, -20,-10,-10, -5, -5,-10,-10,-20]
favourableKing = [-30,-40,-40,-50,-50,-40,-40,-30, -30,-40,-40,-50,-50,-40,-40,-30, -30,-40,-40,-50,-50,-40,-40,-30, -30,-40,-40,-50,-50,-40,-40,-30,-20,-30,-30,-40,-40,-30,-30,-20,-10,-20,-20,-20,-20,-20,-20,-10,20, 20,  0,  0,  0,  0, 20, 20,20, 30, 10,  0,  0, 10, 30, 20]

positionPreferenceMapper = {1 : favourablePawn, -1 : favourablePawn, 3 : favourableKnight, -3 : favourableKnight,
                            4:favourableBishop , -4:favourableBishop , 5:favourableRook, -5:favourableRook,
                            9:favourableQueen, -9:favourableQueen, 200:favourableQueen, -200:favourableQueen}


# Defines the set of valid positions that can be explored with / without capturing a piece
moveIndex = {
                0:None, # Blank Piece
                1:[[(1,0)],2],  # White Pawn
                -1:[[(1,0)],2], # Black Pawn
                3:[[(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)],2], # White Knight
                -3:[[(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)],2], # Black Knight
                4 : [[(1,1),(-1,-1),(1,-1),(-1,1)],9], # White Bishop
                -4 : [[(1,1),(-1,-1),(1,-1),(-1,1)],9], # Black Bishop
                5 : [[(1,0),(0,1),(-1,0),(0,-1)],9], # White Rook
                -5 : [[(1,0),(0,1),(-1,0),(0,-1)],9], # Black Rook
                9 : [[(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)],9],   # White Queen        DRUL
                -9 : [[(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)],9],   # Black Queen
                200 : [[(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)],2],   # White King
                -200 : [[(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)],2]   # Black King
            }
