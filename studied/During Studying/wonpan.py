# N개의 원판
# M개의 정수
# T 번의 경우를 수행한다.
n, m, t=list(map(int, input().split()))
round_thing= []
def rotate(lis, dir, value): # 테스트 완료
    global m

    result=[]
    if dir==0:# 시계방향 + 방향
        for i in range(m):
            result.append(lis[(i-value)%m])
    elif dir==1: # 반시계방향 - 방향
        for i in range(m):
            result.append(lis[(i+value)%m])
    return result

dx= [-1,1,0,0]
dy= [0,0,-1,1]


def near_del():
    result=False
    new_map = [[-1 for _ in range(m)] for _ in range(n)]
    global round_thing
    for i in range(n):
        for j in range(m):
            if round_thing[i][j]!=0:
                for kk in range(4):
                    mi = i + dx[kk]
                    mj = (j + dy[kk])%m
                    if (0 <= mi < n
                            and round_thing[mi][mj] == round_thing[i][j]
                            and round_thing[mi][mj]!=0) :
                        new_map[i][j] = 0
                        new_map[mi][mj]=0
                        result=True
    for i in range(n):
        for j in range(m):
            if new_map[i][j] == 0:
                round_thing[i][j]=0
    return result



for i in range(n):
    round_thing.append(list(map(int, input().split())))

for i in range(t):
    x , d, k = list(map(int, input().split()))

    for i in range(n):
        if (i+1)%x ==0 :
            round_thing[i]=rotate(round_thing[i], d, k)

    delornot=near_del()

    if not delornot: # 없으면
        sum = 0
        count = 0
        for i in range(n):
            for j in range(m):
                if round_thing[i][j] != 0:
                    count+=1
                    sum+= round_thing[i][j]
        avg=0
        if count!=0:
            avg=sum/count

        for i in range(n):
            for j in range(m):
                if round_thing[i][j] != 0:
                    if avg > round_thing[i][j]:
                        round_thing[i][j]+=1
                    elif avg < round_thing[i][j]:
                        round_thing[i][j]-=1

G_SUM=0
for i in range(n):
    for j in range(m):
        G_SUM +=round_thing[i][j]

print(G_SUM)