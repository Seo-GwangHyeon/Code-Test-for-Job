import numpy as np
class Side:
    def __init__(self, c):
        self.board= np.full((3,3 ), c)

# 윗 면은 흰색,
# 아랫 면은 노란색,
# 앞 면은 빨간색,
# 뒷 면은 오렌지색,
# 왼쪽 면은 초록색,
# 오른쪽 면은 파란색
#           B
#           22 21 20
#           12 11 10
#           02 01 00
# L         U         R
# 20 10 00  00 01 02  02 12 22
# 21 11 01  10 11 12  01 11 21
# 22 12 02  20 21 22  00 10 20
#
#        F  00 01 02
#           10 11 12
#           20 21 22
#
#        D  00 01 02
#           10 11 12
#           20 21 22
def getrowcol(board,row, col):
    if row==1 :
        return board[0:1,0:3][0]
    if row == 3:
        return board[2:3, 0:3][0]
    if col==1:
        return np.transpose(board[0:3, 0:1])[0]
    if col==3:
        return np.transpose(board[0:3, 2:3])[0]
import copy as cp;
def clock_roate(n1,n2,n3,n4):
    temp=[0,0,0]
    for i in range(3):
        temp[i]=n1[i]
    for i in range(3):
        n1[i] = n2[i]
    for i in range(3):
        n2[i] = n3[i]
    for i in range(3):
        n3[i] = n4[i]
    for i in range(3):
        n4[i] = temp[i]

def on_rotate(board):
    new_board = np.full((3,3 ), '0')
    for i in range(3):  # 행
        for j in range(3):  # 열
            new_board[j][3 - 1 - i] = board[i][j]
    return new_board

def off_rotate(board):
    new_board = np.full((3,3 ), '0')
    for i in range(3):  # 행
        for j in range(3):  # 열
            new_board[3 - 1 - j][i] = board[i][j]
    return new_board



def rotate(now, clock, cube ):
    r_list=[]
    north = None
    east = None
    south = None
    west = None
    if now=='U':
        r_list=['B', 'R', 'F', 'L']
        # 0:1 , 0:3 뜻 0 ~ 1행과 0 ~ 3 열을 슬라이스
        north=getrowcol(cube[r_list[0]].board, 1,-1)
        east =getrowcol(cube[r_list[1]].board, 1,-1)
        south =getrowcol(cube[r_list[2]].board, 1,-1)
        west =getrowcol(cube[r_list[3]].board, 1,-1)
    elif now=='D':
        r_list=['F','R','B','L']
        north = np.flip(getrowcol(cube[r_list[0]].board, 3,-1))
        east  = np.flip(getrowcol(cube[r_list[1]].board, 3,-1))
        south = np.flip(getrowcol(cube[r_list[2]].board, 3,-1))
        west  = np.flip(getrowcol(cube[r_list[3]].board, 3,-1))
    elif now == 'F':
        r_list=['U','R','D','L']
        north = np.flip(getrowcol(cube[r_list[0]].board, 3,-1))
        east = np.flip(getrowcol(cube[r_list[1]].board, -1,1))
        south = getrowcol(cube[r_list[2]].board, 1,-1)
        west = getrowcol(cube[r_list[3]].board, -1,3)
    elif now == 'B':
        r_list=['U','L','D','R']
        north = getrowcol(cube[r_list[0]].board, 1,-1)
        east = np.flip(getrowcol(cube[r_list[1]].board, -1,1))
        south = np.flip(getrowcol(cube[r_list[2]].board, 3,-1))
        west = getrowcol(cube[r_list[3]].board, -1,3)
    elif now == 'L':
        r_list=['U','F','D','B']
        north = np.flip(getrowcol(cube[r_list[0]].board, -1,1))
        east = np.flip(getrowcol(cube[r_list[1]].board, -1,1))
        south = np.flip(getrowcol(cube[r_list[2]].board, -1,1))
        west = getrowcol(cube[r_list[3]].board, -1,3)

    elif now == 'R':
        r_list=['U','B','D','F']
        north = getrowcol(cube[r_list[0]].board, -1,3)
        east = np.flip(getrowcol(cube[r_list[1]].board, -1,1))
        south = getrowcol(cube[r_list[2]].board, -1,3)
        west = getrowcol(cube[r_list[3]].board, -1,3)
    if clock=='+':
        clock_roate(north, west, south, east)
        cube[now].board = on_rotate(cube[now].board)
    elif clock=='-':
        clock_roate(north, east, south, west)
        cube[now].board = off_rotate(cube[now].board)


dirs = ['U','D','F','B','L','R']
colors=['w','y','r','o','g','b']

#큐브 세팅
n=int(input())
for i in range(n):
    cube = dict();
    for i in range(len(colors)):
        cube[dirs[i]] = Side(colors[i]);
    m=int(input())
    temp=list(map(str, input().split() ))
    moves=list()
    for t in temp:
        moves.append([t[0],t[1]]);
    for m in moves:
        side = m[0]
        clock = m[1]
        rotate(side, clock, cube)
    answer=cube['U'].board
    for ans in answer:
        for a in ans:
            print(a,end='')
        print()


