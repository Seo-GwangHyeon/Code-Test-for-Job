

n= int(input())
board = [[0 for col in range(n)] for row in range(n)]
visited =[[0 for col in range(n)] for row in range(n)]
dx=[-1,0,0,1]
dy=[0,-1,1,0]

for i in range(n):
    board[i] = list(map(int, input().split()))
row=0
col=0
for i in range(n):
    for j in range(n):
        if board[i][j]==9:
            row=i
            col=j
            board[i][j]=0
            visited[i][j] = 1

def seek(row, col, size, time, ate):
    global visited
    global board
    moving = list()
    moving.append([row, col, time])
    min1 = -1
    while(  True ):

        min_x= 12345678
        min_y = 12345678
        min_time = 123456789
        flag=False
        while (len(moving)>0) :
            xy = moving.pop(0)
            # print(xy)
            x = xy[0]
            y = xy[1]
            time = xy[2]
            for i in range(4):
                mov_x = x+dx[i];
                mov_y = y+dy[i];
                mov_time = time +1 ;
                if (mov_x>=0 and mov_x<n
                    and mov_y>=0 and mov_y<n
                    and board[mov_x][mov_y] <= size
                    and visited[mov_x][mov_y] ==0):
                    moving.append([mov_x, mov_y, mov_time])
                    if (board[mov_x][mov_y] >= 1 and  board[mov_x][mov_y] < size):
                        if(min_time > mov_time):
                            min_x = mov_x
                            min_y = mov_y
                            min_time = mov_time
                            flag=True
                        elif(min_time == mov_time ):
                            if(min_x > mov_x):
                                min_x = mov_x
                                min_y = mov_y
                                min_time = mov_time
                                flag = True
                            elif(min_x == mov_x ):
                                if  min_y > mov_y:
                                    min_x = mov_x
                                    min_y = mov_y
                                    min_time = mov_time
                                    flag = True
                    visited[mov_x][mov_y] =1
        # 라운드 별로 하려면 while문 밖에서 append를 하면 round 전체 별로 체크해볼 수 있다.
        if (  flag and board[min_x][min_y] >= 1
                and board[min_x][min_y] < size):
            ate += 1
            visited = [[0 for col in range(n)] for row in range(n)]
            visited[min_x][min_y] = 1
            moving.clear()
            moving.append([min_x, min_y, min_time])
            if (size == ate):
                size += 1
                ate = 0
            board[min_x][min_y] = 0
            min1 = min_time;

        else :
            break;
    return min1

result =seek(row,col,2,0,0)
if result==-1:
    print(0)
else:
    print(result)



