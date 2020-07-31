from collections import deque

dx=[1,-1,0,0]
dy=[0,0,1,-1]

q=deque()
c=[]
def bfs(r, b, n):
    q.append(r)
    c.append(r)
    cnt=0;
    while q:
        qlen=len(q);
        while qlen:
            drone=q.popleft()
            # 목적지 도착
            if drone==[[n-1,n-2],[n-1,n-1]] or drone == [[n-2,n-1],[n-1,n-1]]:
                return cnt;
            for i in range(4):
                temp=[]
                flag=0
                # 2개의 날개
                for j in range(2):
                    nx = drone[j][0]+dx[i];
                    ny = drone[j][1] + dy[i];
                    if 0 <=nx < n and 0 <= ny < n and b[nx][ny]==0:
                        temp.append([nx, ny])
                    else: #
                        flag=1;
                        break;
                if not flag:
                    if drone[0][0] == drone[1][0]:
                        if i==0 or i == 1: # 위아래 움직일 수 있는 경우 돈다.
                            turn(drone, i, '|') # | 모양으로 돌린다.
                    elif drone[0][1] == drone[1][1]:
                        if i==2 or i==3:
                            turn(drone, i, '-')
                    temp.sort();
                    if temp not in c:
                        q.append(temp);
                        c.append(temp);
            qlen-=1
        cnt+=1

def turn(drone, i, mode):
    for j in range(2):
        if mode=='|':
            wing1 = drone[j];
            # y축을 갖게하고 x축을 더 하거나 뺀다.
            wing2 = [drone[j][0]+dx[i], drone[j][1] ]

        elif mode=='-':
            wing1=[drone[j][0], drone[j][1]+dy[i]]
            wing2=drone[j]

        if mode == '|' or mode=='-':
            temp = [wing1, wing2]
            temp.sort()
            if temp not in c:
                q.append(temp);
                c.append(temp);

def solution(board):
    n=len(board);
    robot=[[0,0],[0,1]]
    return bfs(robot, board, n)


print(solution([[0, 0, 0, 1, 1],
                [0, 0, 0, 1, 0],
                [0, 1, 0, 1, 1],
                [1, 1, 0, 0, 1],
                [0, 0, 0, 0, 0]]
))