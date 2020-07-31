n = int(input())
half_n = int(n/2)
players = [[0 for col in range(n)] for row in range(n)]
for i in range(n):
    players[i] = list(map(int, input().split()))

array1=list();
for i in range(n):
    array1.append(i);

min1 = 123456789
team1_socres=list();
team2_socres=list();

def calc():
    team1=0;
    team2=0;
    for i in range (len(team1_socres)):
        for j in range(len(team1_socres)):
            team1+= players[team1_socres[i]][team1_socres[j]]
    for i in range (len(team2_socres)):
        for j in range(len(team2_socres)):
            team2+= players[team2_socres[i]][team2_socres[j]]
    global min1
    if  (abs(team1-team2) < min1 ):
        min1=abs(team1-team2)



def select_team(idx, t1, t2):
    global min1
    if(min1==0):
        return
    if(t1==0 and  t2==0):
        calc();
        return;
    if (idx >= n):
        return;
    if( t1>0 ):
        team1_socres.append(idx);
        select_team(idx+1, t1 -1, t2)
        team1_socres.pop()
    if (t2 > 0):
        team2_socres.append(idx);
        select_team(idx + 1, t1, t2  - 1)
        team2_socres.pop()


select_team(0,half_n, half_n);
print(min1)

