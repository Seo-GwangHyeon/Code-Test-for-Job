from collections import deque
n, l, r= map(int, input().split(' '))

dx=[0,0,-1,1]
dy=[-1,1,0,0]

board=list()
for i in range(n):
    board.append(list(map(int, input().split(' '))))
visited=[[0 for i in range(n)] for j in range(n) ]

dfs=list()
queue=deque()
answer=0
def print_arr(board):
    for b in board:
        print(b)
    print()
def move_xy( i, j,v, k, sums, counts):
    global dfs, dx, dy, n,  l, r,board, visited
    x = i + dx[k]
    y = j + dy[k]
    if ( 0 <= x < n and 0 <= y < n and visited[x][y] == 0 and
         l <= abs(board[x][y] - board[i][j]) <= r):
        visited[i][j] = v
        visited[x][y] = v
        sums[v] += board[x][y]
        counts[v] += 1
        queue.append([x, y])

while(1):
    count_exit=0
    sums = dict()
    counts = dict()
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                v = i * n + j+1
                sums[v] = 0
                counts[v] = 0
                sums[v] += board[i][j]
                counts[v] += 1
                for k in range(4):
                    move_xy(i, j, v, k, sums, counts)
                run = False
                while len(queue) > 0:
                    run = True
                    popped = queue.popleft()
                    _i = popped[0]
                    _j = popped[1]
                    for k in range(4):
                        move_xy( _i, _j, v, k, sums, counts)
                if run:
                    count_exit += 1
    if count_exit==0:
        break
    for i in range(n):
        for j in range(n):
            v=visited[i][j]
            if v != 0:
                board[i][j] = sums[v] // counts[v]
                visited[i][j] = 0
    answer += 1
    if answer==2000:
        break
print(answer)

