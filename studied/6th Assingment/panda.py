import sys
sys.setrecursionlimit(300000)

dx=[-1,1,0,0]
dy=[0,0,-1,1]
n=int(input())
board=[[0 for col in range(n)] for row in range(n)]
days=[[0 for col in range(n)] for row in range(n)]
for i in range(n):
    board[i]=list(map(int, input().split()))
stack=list()

def dfs(x,y):
    if days[x][y]:
        return days[x][y];
    days[x][y]=1
    for i in range(4):
        mx, my = x+dx[i] , y+dy[i];
        if 0<=mx<n and 0<=my<n and board[x][y]<board[mx][my] :
            days[x][y]=max(days[x][y], dfs(mx,my)+1)
    return days[x][y]

for i in range(n):
     for j in range(n):
         days[i][j]=dfs(i,j)
print(max(map(max,days)))

