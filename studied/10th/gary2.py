import sys
read=sys.stdin.readline

n=int(read())
nsum=0
board= []
for i in range(n):
    board.append(list(map(int, read().split())))
    nsum+=sum(board[i])

def divide(x, y, d1, d2, ans):
    while True:
        while True:
            lx, ly, rx, ry = x+d1, y-d1, x+d2, y+d2
            if rx== n-1 or ry== n:
                break
            bx, by = x+d1+d2, y - d1 +d2
            if bx >= n or by >= n or by <0:
                break
            ans = min(ans, get_value(x, y, lx, ly, rx, ry, by))
            d2 +=1
        d1+=1
        if x+d1==n-1 or y - d1 ==-1:
            break
        d2 = 1
    return ans

def get_value(x, y, lx, ly, rx, ry, by):
    counts=[-100,0, 0 , 0, 0, 0]
    d=0
    for i in range(lx):
        for j in range(y+1):
            if[i, j]==[x+d, y-d]:
                d+=1
                break
            counts[1]+= board[i][j]
    d=1
    for i in range(rx+1):
        for j in range(n-1, y, -1):
            if [i,j] ==[x+d, y+d]:
                d+=1
                break
            counts[2]+=board[i][j]
    d=0
    for i in range(lx, n):
        for j in range(by):
            if[i, j] == [lx+d, ly+d]:
                d+=1
                break
            counts[3]+=board[i][j]
    d=1
    for i in range(rx+1, n):
        for j in range(n-1, by-1, -1):
            if [i,j]== [rx+d, ry-d]:
                d+=1
                break
            counts[4]+=board[i][j]
    counts[5]=nsum-sum(counts[1:5])
    # print(counts)
    max_cnt= max(counts[1:6])
    min_cnt = min(counts[1:6])
    # print(max_cnt, min_cnt)
    return max_cnt - min_cnt

ans=sys.maxsize
for i in range(n-2):
    for j in range(1, n-1):
        d1, d2= 1, 1
        ans =min(ans, divide(i, j, d1, d2, ans))

print(ans)