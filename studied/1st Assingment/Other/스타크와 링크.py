from itertools import permutations, combinations
import copy as cp
n = int(input())
half_n = int(n/2)
players = [[0 for col in range(n)] for row in range(n)]
for i in range(n):
    players[i] = list(map(int, input().split()))

array1=list();
for i in range(n):
    array1.append(i);

#print(temp)
temp1 = list(combinations(array1, half_n));
#print(temp1)
min =123456789
for i in range(len(temp1)):
    _array1=cp.deepcopy(array1)
    for j in range(half_n):
        _array1.remove( temp1[i][j] )
    temp2 = list(combinations(_array1, half_n));
    # 탐색 시작
    team1=0;
    tema1_scores=list(combinations(temp1[i], 2))
    for k in range(len(tema1_scores)):
        a=tema1_scores[k][0]
        b=tema1_scores[k][1]
        team1 += players[a][b]
        team1 += players[b][a]
    tema1_scores.clear()
    for j in range(len(temp2)):
        team2 = 0;
        tema2_scores = list(combinations(temp2[j], 2))
        for k in range(len(tema2_scores)):
            a = tema2_scores[k][0]
            b = tema2_scores[k][1]
            team2 += players[a][b]
            team2 += players[b][a]
        if(min > abs(team1-team2)):
            min=abs(team1-team2)
        tema2_scores.clear()
        if(min==0):
            break;
    if(min==0):
        break;
print(min)


