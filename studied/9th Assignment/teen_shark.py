
# 0) 청소년 상어는 (0, 0)에 있는 물고기를 먹고 (0,0)에 들어간다.
# 1) 상어는 자신의 방향으로 가서 물고기를 먹는다.
# 상어의 방향은 먹은 물고기의 방향이 된다.
# 상어가 물고기를 먹은 후에
# 2) 물고기가 이동한다.
#   번호가 작은 물고기부터 순서 대로 이동한다.
#   (1) 물고기가 이동 가능한 경우
#       빈칸 또는 다른 물고기가 있는 칸
#        다른 물고기가 있는 칸으로 이동 할 때는 서로의 위치를 바꾼다.
#   (2) 물고기가 이동 불가능 한 경우
#       상어가 있거나 공간의 경계를 넘는 칸
#       이 경우 반시계 방향으로 45도 회전한다.

#  상어는 방향에 있는 칸으로 이동할 수 있다.
#  한번에 여러 개의 칸을 이동할 수 있다.
#  상어가 이동하면 그 칸의 물고기를 먹고 그 물고기의 방향을 가진다.
#  단, 물고기가 없는 칸으로는 이동할 수 없다.
#  이동 하는 중에 지나가는 칸의 물고기는 먹지 않는다.

# 상어가 먹을 수 있는 물고기 번호의 합의 최댓 값을 구한다.

# 공간의 크기 4 x 4 이고,
# 1부터 순서대로 ↑, ↖, ←, ↙, ↓, ↘, →, ↗
#              1, 2, 3, 4, 5, 6, 7, 8
# 번호, 방향으로 총 4*4의 데이터가 들어온다.
#     ↑,  ↖, ←,  ↙, ↓, ↘, →, ↗
import copy as cp
dx= [-1, -1,  0,  1, 1, 1, 0, -1]
dy= [ 0, -1, -1, -1, 0, 1, 1,  1]
SHARK=999
dir=[1, 2, 3, 4, 5, 6, 7, 8]

class fish:
    def __init__(self,x,y, num, dir):
        self.x=x
        self.y=y
        self.num=num
        self.dir=dir-1
    def show(self):
        print(self.x, self.y, self.num, self.dir)

fishes = dict()
board=[ [0 for _ in range(4)] for _ in range(4) ]
for i in range(4):
    temp=list(map(int, input().split()) )
    for k in range(len(temp)):
        if k%2==0:
            board[i][k//2]=temp[k]
            fishes[temp[k]]= fish(i, k//2, temp[k], temp[k+1])
#fishes = sorted(fishes,key= lambda fish:fish.num )
# for f in fishes:
#     f.show()
# print()


#  first eating
x, y=0, 0
sum = 0

dfs=list()


dfs.append([ [x,y], sum, fishes, board, 0])
max1=-1
while True:
    popped = dfs.pop()
    _x, _y=popped[0]
    _sum=popped[1]
    _fishes = popped[2]
    _board = popped[3]
    __fishes = cp.deepcopy(_fishes)
    __board = cp.deepcopy(_board)

    _dir = __fishes[__board[_x][_y]].dir
    __sum = _sum + __fishes[__board[_x][_y]].num
    max1= max(max1,__sum)

    del (__fishes[__board[_x][_y]])
    __board[_x][_y] = SHARK

    # 물고기 이동
    import copy as cp
    aaa=sorted(_fishes.keys())
    for f in aaa:
        flag= True
        while flag:
            mx = __fishes[f].x + dx[__fishes[f].dir]
            my = __fishes[f].y + dy[__fishes[f].dir]
            if (0 <= mx < 4 and 0 <= my < 4
                    and __board[mx][my] != SHARK):
                flag=False
                # 일단 움직 일 수 있는 경우
                if __board[mx][my]>0:# 물고기가 있는 경우
                    # swap 한다.
                    fx=__fishes[f].x
                    fy=__fishes[f].y
                    __fishes[__board[mx][my]].x = __fishes[f].x
                    __fishes[__board[mx][my]].y = __fishes[f].y
                    __fishes[f].x = mx
                    __fishes[f].y = my

                    temp_num = __board[mx][my]
                    __board[mx][my]=__board[fx][fy]
                    __board[fx][fy] =temp_num
                else: #빈칸 인 경우
                    __board[mx][my]=f
                    __fishes[f].x = mx
                    __fishes[f].y = my
            else: # 가려는 방향으로 갈 수 없는 경우
                __fishes[f].dir= (__fishes[f].dir+1)%8

    # 물고기 이동 끝

    #상어 식사 시작
    for i in range(1, 4):
        _mx = _x + i * dx[_dir]
        _my = _y + i * dy[_dir]
        if (0 <= _mx < 4 and 0 <= _my < 4
                and 0 < __board[_mx][_my] < SHARK):
            __board[_x][_y] = 0
            dfs.append([[_mx, _my], __sum, __fishes, __board, _dir])
    if len(dfs)<=0:
        break

print(max1)


# for f in fishes:
#     f.show()
# print()
#
# for b in board:
#     print(b)
# print()