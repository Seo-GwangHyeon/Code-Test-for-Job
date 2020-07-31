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
    global round_thing
    for i in range(n):
        for j in range(m):
            flag=False
            if round_thing[i][j]!=-1:
                for kk in range(4):
                    mi = i + dx[kk]
                    mj = (j + dy[kk])%4
                    if 0 <= mi < 4 \
                            and round_thing[mi][mj] == round_thing[i][j] \
                            and round_thing[mi][mj]!=-1 :
                        round_thing[mi][mj]=-1
                        flag=True
                        result=True
                if flag:
                    round_thing[i][j]=-1
    return result



for i in range(n):
    round_thing.append(list(map(int, input().split())))

for i in range(t):
    turn= list(map(int, input().split()))
    x , d, k =turn
    for i in range(n):
        if (i+1)%x ==0 :
            round_thing[i]=rotate(round_thing[i], d, k)

    if not near_del(): # 없으면 타노스
        sum = 0
        count = 0
        for i in range(n):
            for j in range(m):
                if round_thing[i][j]!=-1:
                    count+=1
                    sum+= round_thing[i][j]

        avg=sum/count
        for i in range(n):
            for j in range(m):
                if round_thing[i][j] != -1:
                    if avg > round_thing[i][j]:
                        round_thing[i][j]+=1
                    elif avg < round_thing[i][j]:
                        round_thing[i][j]-=1
    # for r in round_thing:
    #     print(r)
    # print()

G_SUM=0
for i in range(n):
    for j in range(m):
        if round_thing[i][j] != -1:
            G_SUM +=round_thing[i][j]

print(G_SUM)