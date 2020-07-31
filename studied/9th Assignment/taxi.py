# n*n
# m 명 승객
# fuel 연료
import copy as cp
dx=[-1,0,1,0]
dy=[0,-1,0,1]

# 입력 부분
n, m, gas = list(map(int, input().split(' ')))
board= list()
for i in range(n):
    temp=list(map(int, input().split(' ') ))
    board.append(temp)
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            board[i][j]=-1;

x, y =list(map(int, input().split(' ')))
x-=1
y-=1
for i in range(m):
    temp=list(map(int, input().split(' ') ))
    board[temp[0]-1][temp[1]-1] = i+1
    board[temp[2]-1][temp[3]-1] = i + 1+1000

# 최단 거리를 찾는



# 일단 시작점 에서 승객들 명단을 보면서 최단거리의 승객을 찾는다.
# 그리고 승객을 찾으면 해당 점에서 다른 점까지의 실제 거리를 구한다.
# 그리고 목적지에 데려다 주고 나면 현재 위치를 바꾼다.
def do_bfs( s_point, condition, gas):
    global n, m, board, dx, dy
    distance=0
    now_point=[-1, -1]
    bfs=list()
    visited = [[0 for _ in range(n)] for _ in range(n)]
    bfs.append([s_point, distance, visited] )
    while len(bfs)>0:
        popped = bfs.pop(0)
        _sp, _dis, _vis = popped

        for i in range(4):
            mx = _sp[0] + dx[i]
            my = _sp[1] + dy[i]
            if ( 0 <= mx <n and 0 <= my <n
                    and _vis[mx][my] == 0 and board[mx][my] != -1) :
                # 아무 시작 승객 찾기
                if condition == 10 and 1 <= board[mx][my] < 1000:
                    value = board[mx][my]
                    board[mx][my] = 0
                    m-=1
                    return [[mx, my], _dis, value]
                # 목적지로 가기
                elif condition >= 1001 and condition == board[mx][my]:
                    board[mx][my] = 0
                    m -= 1
                    return [[mx, my], _dis, 9999]
                __vis=cp.deepcopy(_vis)
                __vis[mx][my]=1
                bfs.append([[mx,my], _dis+1, __vis])
                if _dis > gas:
                    return [now_point, -100, -999]
        # for v in _vis:
        #     print(v)
        # print()
    return [ now_point, -100 ,-999 ]

# 일단 시작점 에서 승객들 명단을 보면서 최단거리의 승객을 찾는다.
# 그리고 승객을 찾으면 해당 점에서 다른 점까지의 실제 거리를 구한다.
# 그리고 목적지에 데려다 주고 나면 현재 위치를 바꾼다.
for _ in range(m):
    # 택시 찾기
    result= do_bfs([x,y] , 10, gas)
    if result[2]== -999:
        gas = -1
        break
    x, y = result[0]
    #print("find", x, y, "gas : ", result[1])
    gas -= result[1]
    #print("gas used", x, y, "gas : ", result[1])
    index = result[2]
    if gas < 0:
        gas = -1
        break
    # 목적지 가기
    result = do_bfs([x, y], 1000+index , gas)
    # print("taxi go", x, y, "gas : ", result[1])
    if result[2]== -999:
        gas = -1
        break
    x, y = result[0]
    # print("object", x, y)
    gas += result[1]
    # print("gas refill", x, y, "gas : ", result[1])
    if gas-(2*result[1])<0:
        gas=-1
        break

print(gas)

