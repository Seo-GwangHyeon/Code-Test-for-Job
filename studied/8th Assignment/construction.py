dx=[1,-1,0,0]
dy=[0,0,1,-1]

def solution(board):
    n=len(board)
    dp = [[10000 for _ in range(n)] for _ in range(n)]
    min_val=10000
    dfs=list()
    for i in range(4):
        mx = 0 + dx[i]
        my = 0 + dy[i]
        if (0 <= mx < n and 0 <= my < n
            and board[mx][my] == 0 and 0 < dp[mx][my]):
            # 현재 비용이 dp보다 크면 안함
            isUD = (i == 0 or i == 1)
            isLR = (i == 2 or i == 3)
            dir = -1
            if isUD:  # 위 아래인 경우
                dir = 0  # 세로
            elif isLR:  # 좌우 인 경우
                dir = 1  # 가로
            dp[mx][my] = 1
            dfs.append([mx, my, dir, 1])

    while( len(dfs)>0 ):
        popped=dfs.pop(0)
        _x, _y, _dir, _cost = popped
        if(_x == n-1 and _y==n-1):
            min_val=min(min_val, _cost)
        for i in range(4):
            mx = _x + dx[i]
            my = _y + dy[i]
            if (0<= mx < n and 0<=my<n
                and board[mx][my]==0 and _cost < dp[mx][my]) :
                #현재 비용이 dp보다 크면 안함
                isUD= (i == 0 or i == 1)
                isLR= (i == 2 or i == 3)
                __cost=0+_cost
                __dir=0+_dir
                if __dir==0 and isLR: # 세로 일때 좌우인 경우
                    __dir=1 # 가로로 전환
                    __cost+=5
                elif __dir==1 and isUD: # 가로일 때 상하인 경우
                    __dir=0 # 세로로 전환
                    __cost += 5
                __cost += 1
                dp[mx][my]=__cost
                dfs.append([mx, my, __dir,  __cost])
    return min_val*100

#
result=solution([[0,0,0,0,0,0,0,1],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,1,0,0],
                 [0,0,0,0,1,0,0,0],
                 [0,0,0,1,0,0,0,1],
                 [0,0,1,0,0,0,1,0],
                 [0,1,0,0,0,1,0,0],
                 [1,0,0,0,0,0,0,0]])
# result=solution([[0,0,0],[0,0,0],[0,0,0]])
print(result)