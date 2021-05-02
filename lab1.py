print ("Enter the number of Queens")
N = int(input())

chessboard = [[0]*N for _ in range(N)]

def is_attack(i, j):
    #checking row or column
    for k in range(0,N):
        if chessboard[i][k]==1 or chessboard[k][j]==1:
            return True
    #checking diagonals
    for k in range(0,N):
        for l in range(0,N):
            if (k+l==i+j) or (k-l==i-j):
                if chessboard[k][l]==1:
                    return True
    return False

def N_queen(n):
    if n==0:
        return True
    for i in range(0,N):
        for j in range(0,N):
            if (not(is_attack(i,j))) and (chessboard[i][j]!=1):
                chessboard[i][j] = 1
                #verify arrangment
                if N_queen(n-1)==True:
                    return True
                chessboard[i][j] = 0
    return False

N_queen(N)
for i in chessboard:
    print (i)