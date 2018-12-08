import copy
def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    for r in board:
        h={}
        for i,x in enumerate(r):
            if(x == "."): continue
            if(x not in h):
                h[x] = i
            else:
                return False
    board2 = copy.deepcopy(board)
    for i in range(9):
        for j in range(9):
            board2[i][j] = board[j][i]
    for i in board:
        print("\t".join(i))
    for r in board2:
        h={}
        for i,x in enumerate(r):
            if(x == "."): continue
            if(x not in h):
                h[x] = i
            else:
                return False
    print("\n\n")
        print("\t".join(i))


    for i in range(3):
        for j in range(3):
            ptx = 3 * i
            pty = 3 * j
            h = {}
            for x in range(ptx,ptx + 3):
                for y in range(pty,pty + 3):
                    c = board[x][y]
                    if c == ".":
                        continue
                    elif c not in h:
                        h[c] = i
                    else:
                        return False
    return True

input = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
a = isValidSudoku(input)
print(a)