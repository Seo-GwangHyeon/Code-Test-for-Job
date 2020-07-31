
def travel_row(board, n,l,i, _from, _to, _rd=1):
    count = 1
    total_count=0
    visited = [0 for col in range(n)]
    for j in range(_from, _to, _rd):
        if board[i][j] == board[i][j + _rd]:
            count += 1;
        elif abs(board[i][j]- board[i][j + _rd])==1:
            if( board[i][j] < board[i][j + _rd] and visited[j]==0) :
                if (count >= l):
                    flag=True;
                    for _j in range(j, j - l, -1 ):
                        if( board[i][_j] != board[i][j] or visited[_j]!=0 ):
                            flag=False;
                    if(flag== True):
                        for _j in range(j, j - l, -1 ):
                            visited[_j] = 1;
                        total_count += count;
            elif (board[i][j] > board[i][j + _rd] and visited[j + _rd] == 0):
                if( j + l < n ):
                    _count=0;
                    for _j in range(j + _rd, j + l+1, 1):
                        if(board[i][_j] == board[i][j + _rd] and visited[_j]==0):
                            _count+=1;
                    if( _count>=l):
                        total_count += count
                        for _j in range(j + _rd, j + l + 1, 1):
                            visited[_j]=1;
            count = 1;
    total_count += count
    if total_count == n:
        return 1
    return 0;

def solution(board,n,l):
    result=0
    for i in range(n):
        value=travel_row(board, n,l, i,0, n-1, 1 );
        result+=value;
    return result

result=0
n, l= map(int, input().split())
board1 = [[0 for col in range(n)] for row in range(n)]
board2 = [[0 for col in range(n)] for row in range(n)]
for i in range(n):
    board1[i] = list(map(int, input().split()))
result +=solution(board1, n, l)
for i in range(n):
    for j in range(n):
        board2[j][i]=board1[i][j];
result +=solution(board2, n, l)
print(result)