import sys
read = sys.stdin.readline
def comb(a, b):
    result = 1
    if a-b < b:
        b = a-b
    for i in range(a-b+1, a+1):
        result *= i
    for j in range(1, b+1):
        result //=j
    return result

n=int(input())

lists= [0 for _ in range(n)]
edge=[]
for i in range(n-1):
    a, b = list(map(int, read().split() ))
    lists[a - 1]+=1
    lists[b - 1]+=1
    edge.append([a-1,b-1])

d=0
g=0

for e in edge:
    d += (lists[e[0]]-1) * (lists[e[1]]-1)

for i in range(n ):
    if lists[i] >=3:
        g += comb(lists[i], 3)
if d < g*3:
    print("G")
elif d > g*3:
    print("D")
elif d == g*3:
    print("DUDUDUNGA")

