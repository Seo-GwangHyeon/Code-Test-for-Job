nn= int(input())
dx=[-1,1,0,0]
dy=[0,0,-1,1]
import copy as cp
for i in range(nn):
    n=int(input());
    board= list()
    visited = [[0 for col in range(n)] for row in range(n)]
    bd = [[0 for col in range(n)] for row in range(n)]
    for j in range(n):
        board.append(str( input() ))
    for j in range(n):
        for k in range(n):
            bd[j][k]=int(board[j][k])
    path=list();
    path.append([0,0,0, visited])
    min1=123456789
    sum1=0
    while len(path)>0:
        f=path.pop(0);
        x=f[0]
        y = f[1]
        sum1 = f[2]
        vis = f[3]
        if x==n-1 and y==n-1:
            min1=min(min1, sum1)
        temp = list()
        for i in range(4):
            mx= x + dx[i]
            my = y + dy[i]
            _vis=cp.deepcopy(vis)
            if( mx>=0 and mx < n and my >=0 and my < n
            and _vis[mx][my]!=1 and sum1 >= bd[mx][my]):
                _vis[mx][my]=1;
                path.append([mx, my, sum1+bd[mx][my], _vis ])
        # if len(temp) > 0 :
        #     _min= min(temp, key= lambda x:x[2] )
        #     _min[3][_min[0]][_min[1]]=1
        #     path.append(_min)
    print(min1)



