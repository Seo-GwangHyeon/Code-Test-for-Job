# N*N 의 격자에 M개의 칸에 상어가 있다.

# 1초마다 모든 상어가 동시에 상하좌우 인접한 칸 중 하나로 이동하고 자신의 냄새를 그 칸에 뿌린다.
# 이 냄새는 k번 이동(k초 아님)하고 나면 사라진다.

# 아무 냄새가 없는 칸의 방향으로 잡는다.
# 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향을 잡는다.
# 가능한 칸이 여러 칸일 수 있는데 이때 특정한 우선순위를 따른다.
# 한칸에 여러 마리의 상어가 남아 있으면
# 가장 작은 번호를 상어를 제외하고 모두 격자 밖으로 쫓겨난다.

# 1번 상어만 격자에 남게 되기까지 몇초 걸리는지?
# 1000초 넘으면 -1 출력

# 입력
# N  M K
# 첫번째 줄은 위를 향할 때의 방향 우선순위
# 두 번째 줄은 아래를 향할 때의 우선순위,
# 세 번째 줄은 왼쪽을 향할 때의 우선순위,
# 네 번째 줄은 오른쪽을 향할 때의 우선순위
# 1, 2, 3, 4는 각각 위, 아래, 왼쪽, 오른쪽
dx = [-1, 1, 0, 0]
dy = [0,  0,-1, 1]
class shark:
    def __init__(self, num, xy, dir, up, down, left, right):
        self.num = num
        self.xy=xy
        self.dir=dir
        self.prio =[up, down, left, right]
        self.round=0
n, m, k = map(int, input().split())
board=list()
for i in range(n):
    temp = list(map(int, input().split()))
    board.append(temp)
xys=list()
for i in range(n):
    for j in range(n):
        if board[i][j]>0:
            board[i][j]=k*1000+board[i][j]
            xys.append([i,j,board[i][j]])
xys=sorted(xys, key= lambda x:x[2])

s_dir=4
priority=[1,4,2,3]
print((priority.index(s_dir)+1)%4 +1)
s_dir=  priority[(priority.index(s_dir)+1)%4]
print(s_dir)

dirs = list(map(int, input().split()))
sharks=list()
for j in range(m):
    up=list(map(int, input().split()))
    down=list(map(int, input().split()))
    left=list(map(int, input().split()))
    right=list(map(int, input().split()))
    sharks.append(shark(j+1, xys[j],  dirs[j], up,down,left,right))

for b in board:
    print(b)
print()
#상어 move
for absd in range(1,1001):
    # 각 상어들을 움직인다.
    # 냄새는 1초에 1000으로 표시
    # 예시 ) 1번이 냄새를 뿌린 곳 k*1000 + 1
    for i in range(n):
        for j in range(n):
            if board[i][j] > 1000:
                board[i][j] -= 1000
                if board[i][j] < 1000:
                    board[i][j] = 0
    if absd < 10:
        for b in board:
            print(b)
        print()
    for s in sharks:
        flag = True
        for kk in range(4):
            mx = s.xy[0] + dx[s.dir - 1]
            my = s.xy[1] + dy[s.dir - 1]
            if 0 <= mx < n and 0 <= my < n:
                if board[mx][my] == 0:
                    # 냄새 뿌린다.
                    # print("냄새")
                    board[mx][my] = (k) * 1000 + s.num
                    s.xy[0] = mx
                    s.xy[1] = my
                    s.round += 1
                    flag = False
                elif (board[mx][my] % 1000) == s.num:
                    board[mx][my] = (k) * 1000 + s.num
                    s.xy[0] = mx
                    s.xy[1] = my
                    s.round += 1
                    flag = False
                # 상어 만났을 때
                elif board[mx][my] > k * 1000:
                    index = board[mx][my] - k * 1000 - 1
                    s.round += 1
                    if s.num > sharks[index].num:
                        sharks.remove(s)
                        print("len(sharks)", len(sharks))
                    else:
                        sharks.remove(sharks[index])
                        print("len(sharks)", len(sharks))
                        s.xy[0] = mx
                        s.xy[1] = my
                        board[mx][my] = (k) * 1000 + s.num

                    flag = False
            if flag:
                priority = s.prio[s.dir - 1]
                s.dir = priority[(priority.index(s.dir) + 1) % 4]
            else:
                break
    # 냄새 상쇄?
    if absd<10:
        for b in board:
            print(b)
        print()
    # result=0
    # for i in range(n):
    #     for j in range(n):
    #         if board[i][j]>=k*1000:
    #             result+=1
    # if result==1:
    #     break
    if len(sharks)==1:
        break

if absd >= 1000:
    print(-1)
else:
    print(absd)