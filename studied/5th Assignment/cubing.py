
class Side:
    def __init__(self, c):
        self.board= [[c for col in range(3)] for row in range(3)]

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
def flip(board):
    return [board[2],board[1],board[0]]

def getrowcol(board,row, col):
    if row==1 :
        return [[0,0],[0,1],[0,2]]
    if row == 3:
        return [[2,0],[2,1],[2,2]]
    if col==1:
        return [[0,0],[1,0],[2,0]]
    if col==3:
        return [[0,2],[1,2],[2,2]]
import copy as cp;
def clock_roate(cube, rlist,n1,n2,n3,n4):
    temp=["z","z","z"]
    for i in range(3):
        temp[i]=cube[rlist[0]].board[n1[i][0]][n1[i][1]]
    for i in range(3):
        cube[rlist[0]].board[n1[i][0]][n1[i][1]]\
            =cube[rlist[1]].board[n2[i][0]][n2[i][1]]
    for i in range(3):
        cube[rlist[1]].board[n2[i][0]][n2[i][1]] \
            = cube[rlist[2]].board[n3[i][0]][n3[i][1]]
    for i in range(3):
        cube[rlist[2]].board[n3[i][0]][n3[i][1]] \
            = cube[rlist[3]].board[n4[i][0]][n4[i][1]]
    for i in range(3):
        cube[rlist[3]].board[n4[i][0]][n4[i][1]] \
            = temp[i]

def on_rotate(board):
    new_board = [['0' for col in range(3)] for row in range(3)]
    for i in range(3):  # 행
        for j in range(3):  # 열
            new_board[j][3 - 1 - i] = board[i][j]
    return new_board

def off_rotate(board):
    new_board = [['0' for col in range(3)] for row in range(3)]
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
        north=getrowcol(cube[r_list[0]].board, 1,-1)
        east =getrowcol(cube[r_list[1]].board, 1,-1)
        south =getrowcol(cube[r_list[2]].board, 1,-1)
        west =getrowcol(cube[r_list[3]].board, 1,-1)
    elif now=='D':
        r_list=['F','R','B','L']
        north = flip(getrowcol(cube[r_list[0]].board, 3,-1))
        east  = flip(getrowcol(cube[r_list[1]].board, 3,-1))
        south = flip(getrowcol(cube[r_list[2]].board, 3,-1))
        west  = flip(getrowcol(cube[r_list[3]].board, 3,-1))
    elif now == 'F':
        r_list=['U','R','D','L']
        north = flip(getrowcol(cube[r_list[0]].board, 3,-1))
        east = flip(getrowcol(cube[r_list[1]].board, -1,1))
        south = getrowcol(cube[r_list[2]].board, 1,-1)
        west = getrowcol(cube[r_list[3]].board, -1,3)
    elif now == 'B':
        r_list=['U','L','D','R']
        north = getrowcol(cube[r_list[0]].board, 1,-1)
        east = flip(getrowcol(cube[r_list[1]].board, -1,1))
        south = flip(getrowcol(cube[r_list[2]].board, 3,-1))
        west = getrowcol(cube[r_list[3]].board, -1,3)
    elif now == 'L':
        r_list=['U','F','D','B']
        north = flip(getrowcol(cube[r_list[0]].board, -1,1))
        east = flip(getrowcol(cube[r_list[1]].board, -1,1))
        south = flip(getrowcol(cube[r_list[2]].board, -1,1))
        west = getrowcol(cube[r_list[3]].board, -1,3)

    elif now == 'R':
        r_list=['U','B','D','F']
        north = getrowcol(cube[r_list[0]].board, -1,3)
        east = flip(getrowcol(cube[r_list[1]].board, -1,1))
        south = getrowcol(cube[r_list[2]].board, -1,3)
        west = getrowcol(cube[r_list[3]].board, -1,3)
    if clock=='+':
        clock_roate(cube, [r_list[3], r_list[2], r_list[1], r_list[0]]
                    , west, south, east, north)
        cube[now].board = on_rotate(cube[now].board)
    elif clock=='-':
        clock_roate(cube, r_list, north, east, south,west )
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





