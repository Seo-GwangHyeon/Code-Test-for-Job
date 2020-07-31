dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

import copy as cp


def boom(board, x, y, w,h):
    global dx
    global dy
    length = board[x][y];
    board[x][y] = 0;
    if(length<=1):
        return;
    for i in range(1, length):
        for j in range(4):
            mov_x = x + dx[j]*i
            mov_y = y + dy[j]*i
            if( mov_x>=0 and mov_x<h
                    and mov_y>=0 and mov_y<w
                and board[mov_x][mov_y]>0):
                boom(board,mov_x,mov_y,w,h)

def clearing(board, w, h):
    stack=list();
    for i in range(w):
        for j in range(h):
            if board[j][i]!=0:
                stack.append(board[j][i])
                board[j][i]=0;
        j = h - 1;
        while len(stack) > 0:
            board[j][i] = stack.pop()
            j -= 1;

def breaking(board, x, w, h):
    for i in range(h):
        if board[i][x]>0:
            boom(board,i,x,w,h);
            break;
    clearing(board, w, h)

def cal_value(board):
    result=0;
    for bdi in board:
        for i in bdi:
            if i !=0:
                result+=1;
    return result

def bfs(board,n,w,h):

    queue=list()
    depth=1
    for i in range(w):
        _board = cp.deepcopy(board)
        breaking(_board, i, w, h)
        queue.append([i, _board, depth]);

    min1=w*h

    while True:
        _front=queue.pop(0);
        _i=_front[0]
        _bd = _front[1]
        _depth = _front[2]

        min1=min(cal_value(_bd), min1)
        if(min1==0):
            break;

        if (_depth > n):
            break;

        for i in range(w):
            __bd = cp.deepcopy(_bd)
            del _bd
            breaking(__bd, i, w, h)
            queue.append([i, __bd, _depth + 1]);

    return min1;

T = input()
for i in range(int(T)):
    N, W, H = map(int, input().split())
    board = [[0 for col in range(W)] for row in range(H)]

    for j in range(H):
        board[j] = list(map(int, input().split()))

    board_temp=cp.deepcopy(board)
    print(i+1, bfs(board_temp,N, W, H));







