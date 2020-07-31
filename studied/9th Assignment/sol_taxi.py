from collections import deque
import sys

input= sys.stdin.readline
dx=[1, -1, 0, 0]
dy=[0,0,1,-1]

# cnt에 이동거리를 저장하면서 현재 이동 거리에서 이동할 수 있는 만큼 이동한다
# fuel이 cnt보다 작으면 0을 리턴한다
# 이동한 칸에 승객이 있으면 p에 승객의 좌표를 저장한다
# p에 탑승할 승객의 좌표가 있으면 break 해서 while 문을 빠져나간다
# while문을 나오고 p가 비어있으면 승객한테 이동할 수 없는 경우이므로 0을 리턴한다
def bfs1(x, y):
    global fuel
    q1.append([x, y])
    visitd[x][y], cnt= 1, 0
    while q1:
        qlen = len(q1)
        client=[] # p는 갈 곳 찾는 것
        cnt+=1
        if cnt >= fuel:
            return 0
        for _ in range(qlen):
            x, y = q1.popleft()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if (0 <= nx < n and 0 <= ny <n
                        and board[nx][ny] != -1 and visitd[nx][ny] ==0):
                    if board[nx][ny] >0:
                        client.append([nx, ny])
                    q1.append([nx, ny])
                    visitd[nx][ny]=1
        if client:# p가 하나라도 나왔으면 종료?
            break
    if not client: # while문 종료 후에 p가 없으면 승객을 찾지 못하는 경우이다.
        return 0

    fuel -= cnt
    client = sorted(client)
    x, y = client[0]
    # 목적지 까지 거리 구한다.
    res = bfs2(x, y, board[x][y])
    if res==0:
        return 0

    length, nx, ny =res
    fuel += length
    board[x][y]=0
    return nx, ny

# 탐색 중간에 fuel이 이동 거리보다 작거나, 목적지로 이동할 수 없으면 0을 리턴한다
# 목적지로 이동할 수 있으면 이동거리, 목적지 좌표를 리턴한다

def bfs2(x, y, idx):
    q2.append([x,y])
    distances[x][y]=0
    while q2:
        x, y = q2.popleft()
        if distances[x][y] >= fuel:
            return 0
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if (0 <= nx < n and 0 <= ny < n
                    and board[nx][ny] != -1 and distances[nx][ny] ==-1):
                q2.append([nx, ny])
                distances[nx][ny] = distances[x][y] + 1
                if [nx, ny] == d[idx]:
                    return distances[nx][ny], nx, ny
    return 0


n, m, fuel= map(int, input().split())
board=[]
for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(n):
        if board[i][j] ==1:
            board[i][j]=-1

x, y = map(int, input().split())
x-=1
y-=1
# destination
d = [[] for _ in range(m+1)]
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    board[x1-1][y1-1] = i+1
    d[i+1] = [x2-1, y2-1 ]


for _ in range(m):
    q1, visitd = deque(), [[0 for _ in range(n)] for _ in range(n)]
    q2, distances = deque(), [[-1 for _ in range(n)] for _ in range(n)]

    if board[x][y]>0:
        res=bfs2(x,y,board[x][y])
        if res == 0:
            print(-1)
            sys.exit()
        length, nx, ny=res
        if length > fuel:
            print(-1)
            sys.exit()
        fuel+=length
        board[x][y]=0
        x, y = nx, ny
        continue

    res = bfs1(x, y)
    if res==0:
        print(-1)
        sys.exit()
    else:
        x, y =res
print(fuel)
