
dx=[-1,1,0,0]
dy=[0,0,-1,1]

n= int(input())
board = [[0 for col in range(n)] for row in range(n)]

REALMAX=0
for i in range(n):
    board[i] = list(map(int, input().split()))

for bd in board:
    for a in bd:
        REALMAX+=a;

def merge_stack(stack):
    new_stack=list()
    for i in range(0, len(stack)-1, 2):
        if stack[i] == stack[i+1]:
            stack[i] = stack[i]+stack[i+1];
            stack[i+1]=0;
    for i in range(len(stack)):
        if stack[i] != 0:
            new_stack.append(stack[i]);
    return new_stack;


def move(_dx,_dy, board, n):
    stack = list();
    if _dx == -1:
        for j in range(n):
            for i in range(n-1,-1,-1):
                if board[i][j] != 0:
                    stack.append(board[i][j]);
                    board[i][j] = 0;
            stack=merge_stack(stack)
            i = 0;
            while len(stack) > 0:
                board[i][j] = stack.pop()
                i += 1;
    elif _dx==1:
        for j in range(n):
            for i in range(n):
                if board[i][j]!=0:
                    stack.append(board[i][j]);
                    board[i][j]=0;
            stack = merge_stack(stack)
            i=n-1;
            while len(stack)>0:
                board[i][j]=stack.pop()
                i-=1;
    elif _dy == -1:
        for j in range(n):
            for i in range(n-1,-1,-1):
                if board[j][i] != 0:
                    stack.append(board[j][i]);
                    board[j][i] = 0;
            stack = merge_stack(stack)
            i = 0;
            while len(stack) > 0:
                board[j][i] = stack.pop()
                i += 1;
    elif _dy == 1:
        for j in range(n):
            for i in range(n):
                if board[j][i] != 0:
                    stack.append(board[j][i]);
                    board[j][i] = 0;
            stack = merge_stack(stack)
            i = n - 1;
            while len(stack) > 0:
                board[j][i] = stack.pop()
                i -= 1;


def getMax(_board):
    result=-1
    for bd in _board:
        result=max(result,max(bd));
    return result

for i in range(11):
    if pow(2,i)>REALMAX:
        REALMAX=pow(2,i-1)
        break

import copy as cp
def bfs(board,n):
    global dx
    global dy
    global REALMAX
    queue=list()
    depth=1
    for i in range(4):
        _board = cp.deepcopy(board)
        move(dx[i], dy[i], _board, n)
        queue.append([dx[i], dy[i], _board, depth]);

    max1=-1
    count=1
    while True:
        _front=queue.pop(0);
        _dx=_front[0]
        _dy = _front[1]
        _bd = cp.deepcopy(_front[2])
        _depth = _front[3]

        if (_depth > 5):
            break;

        for i in range(4):
            count += 1
            __bd = cp.deepcopy(_bd)
            move(dx[i], dy[i], __bd, n)
            _value=getMax(__bd);
            max1=max(max1,_value)
            queue.append([dx[i], dy[i], __bd,_depth+1]);
        if(max1>=REALMAX):
            break;

    return max1;


print(bfs(board,n))