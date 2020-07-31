
dx=[-1,1,0,0]
dy=[0,0,-1,1]

import copy as cp


def movable(board,visited,n,x,y ,dir):
    global dx, dy;
    # 0 1 2 3
    # U D L R
    mov_x = x +dx[dir];
    mov_y = y + dy[dir];
    if ( mov_x >= 0 and mov_x < n
        and mov_y >= 0 and mov_y < n
        and board[mov_x][mov_y]==0
        and visited[mov_x][mov_y]==0 ) :
        return True;
    return False;

def drone_movable(board,visited,n,left, right, dir):
    if(movable(board, visited, n, left[0], left[1], dir) and
    movable(board, visited, n, right[0], right[1], dir)):
        return True;
    return False;
def go_drone(left, right, board, visited, dir):
    global dx,dy;
    visited[left[0]][left[1]] = 1
    visited[right[0]][right[1]] = 1
    left[0] +=dx[dir];
    left[1] += dy[dir];
    right[0] += dx[dir];
    right[1] += dy[dir];

def VorH(left, right):
    if(left[0] == right[0]):
        return "V"
    return "H"

def turn(board, visited, left, right, dir, q, time):
    _left1 = cp.deepcopy(left);
    _right1 = cp.deepcopy(right);
    _left2 = cp.deepcopy(left);
    _right2 = cp.deepcopy(right);
    _visited = cp.deepcopy(visited);

    if VorH(left,right) == "V":  # 세로일때
        if dir==2 or dir ==3:
            _visited[left[0]][left[1]] = 1
            _visited[right[0]][right[1]] = 1
        if dir ==2: # 왼쪽 부분
            _left1[0] = left[0]- 1
            _left1[1] = left[1]- 1
            q.append( [_left1,_right1, board, _visited,time+1]  )

            _right2[0] = right[0] - 1
            _right2[1] = right[1] + 1
            q.append([_left2, _right2, board, _visited, time + 1])
        elif dir==3:# 오른쪽 부분
            _left1[0] = left[0] + 1
            _left1[1] = left[1] - 1
            q.append([_left1, _right1, board, _visited, time + 1])

            _right2[0] = right[0] + 1
            _right2[1] = right[1] + 1
            q.append([_left2, _right2, board, _visited, time + 1])

    elif VorH(left,right) == "H":  # 세로일때
        if dir ==0 or dir==1:
            _visited[left[0]][left[1]] = 1
            _visited[right[0]][right[1]] = 1

        if dir == 0:
            _left1[0] = left[0] + 1
            _left1[1] = left[1] - 1
            q.append([_left1, _right1, board, _visited, time + 1])

            _right2[0] = right[0] - 1
            _right2[1] = right[1] - 1
            q.append([_left2, _right2, board, _visited, time + 1])

        elif dir == 1:
            _left1[0] = left[0] + 1
            _left1[1] = left[1] + 1
            q.append([_left1, _right1, board, _visited, time + 1])

            _right2[0] = right[0] - 1
            _right2[1] = right[1] + 1
            q.append([_left2, _right2, board, _visited, time + 1])
def setLR(left, right):
    if VorH(left,right) == "V" and left[1]<right[1]:
        temp = cp.copy(left)
        left = cp.copy(right)
        right = temp
        print("switch")

    elif VorH(left, right) == "H" and left[0] > right[0]:
        temp = cp.copy(left)
        left = cp.copy(right)
        right = temp
        print("switch")
def solution(board):
    n=len(board)
    visited=[[0 for col in range(n)] for row in range(n)];
    q=list();
    left = [0, 0]
    right = [1, 0]
    q.append([left,right,board,visited,0])
    min1=n*n;
    while True:
        last= q.pop()
        _left=last[0]
        _right=last[1]
        _board=last[2]
        _visited=last[3]
        _time =last[4]
        print(_left,_right)
        setLR(_left,_right)
        print(_left, _right)
        print()

        if(( _left[0] == n-1 and _left[1]==n-1)
            or ( _right[0] ==n-1 and _right[1]==n-1)):
            min1=min(min1,_time);
            #print(min1)

        for i in range(4):
            if drone_movable(_board,_visited, n , _left, _right, i):
                #print(_left, _right);
                __board = cp.deepcopy(_board)
                __visited = cp.deepcopy(_visited)
                __left=cp.deepcopy(_left)
                __right = cp.deepcopy(_right)
                go_drone(__left, __right, __board, __visited, i)
                q.append([__left, __right, __board, __visited, _time+1])
                turn(_board, _visited, _left, _right, i, q, _time)

        #print("q size ", len(q));
        if (len(q)<=0):
            break;
    answer = min1
    return answer

answer=solution(
[[0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0]])

print(answer)