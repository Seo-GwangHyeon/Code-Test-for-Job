# 0은 호수
# 1은 배양액을 뿌릴 수 없는 땅
# 2는 배양액을 뿌릴 수 있는 땅
# 6 6 3 3
from itertools import combinations

def print_arr(_a):
    for i in range(n):
        print(_a[i])
    print()

# 제외시키는 함수
def delete(arr, _temp):
    for i in range(len(_temp)):
        arr.remove(_temp[i]);

def sum_board(_bd):
    sum=0;
    for i in range(len(_bd)):
        for j in range(len(_bd[i])):
            if(_bd[i][j]==9):
                sum+=1
    return sum;

def expand_green(_bd,_rd, rd_count, i, j):
    flag=1;
    if (i - 1 >= 0):
        if(_bd[i - 1][j] == 1):
            _bd[i - 1][j] = 3;
            _rd[i - 1][j] = rd_count;
            flag=0;
        elif (_bd[i - 1][j] == 4 and _rd[i - 1][j] == round_count):
            _bd[i - 1][j] = 9;
    if (j - 1 >= 0):
        if(_bd[i][j - 1] == 1):
            _bd[i][j - 1] = 3;
            _rd[i][j -1 ] = rd_count;
            flag = 0;
        elif (_bd[i][j - 1] == 4  and _rd[i ][j -1] == round_count):
            _bd[i][j - 1] = 9;
    if (i + 1 < n ):
        if(_bd[i + 1][j] == 1):
            _bd[i + 1][j] = 3;
            _rd[i + 1][j] = rd_count;
            flag = 0;
        elif (_bd[i + 1][j] == 4 and _rd[i + 1][j] == round_count):
            _bd[i + 1][j] = 9;
    if (j + 1 < m):
        if(_bd[i][j  + 1] == 1):
            _bd[i][j + 1] = 3;
            _rd[i][j + 1] = rd_count;
            flag = 0;
        elif (_bd[i ][j + 1] == 4  and _rd[i][j+1] == round_count):
            _bd[i][j + 1] = 9;
    return flag;
def expand_red(_bd, _rd, rd_count, i, j):
    flag = 1;
    if (i - 1 >= 0 ):
        if (_bd[i - 1][j] == 1):
            _bd[i - 1][j] = 4;
            _rd[i - 1][j] = rd_count;
            flag = 0;
        elif (_bd[i - 1][j] == 3 and _rd[i - 1][j] == round_count ):
            _bd[i - 1][j] = 9;

    if (j - 1 >= 0):
        if( _bd[i][j - 1] == 1):
            _bd[i][j - 1] = 4;
            _rd[i][j - 1] = rd_count;
            flag = 0;
        elif (_bd[i][j - 1] == 3  and _rd[i ][j -1] == round_count):
            _bd[i][j - 1] = 9;
    if (i + 1 < n):
        if(_bd[i + 1][j] == 1):
            _bd[i + 1][j] = 4;
            _rd[i + 1][j] = rd_count;
            flag = 0;
        elif (_bd[i + 1][j] == 3  and _rd[i + 1][j] == round_count):
            _bd[i + 1][j] = 9;
    if (j + 1 < m):
        if(_bd[i][j + 1] == 1):
            _rd[i][j + 1] = rd_count;
            _bd[i][j + 1] = 4;
            flag = 0;
        elif (_bd[i ][j + 1] == 3  and _rd[i][j+1] == round_count):
            _bd[i][j + 1] = 9;
    return flag

def change_board(_bd, _rd, rd_count):
    sum=0;
    eval_sum = 0;
    check_one=0;
    for i in range(n):
        for j in range(m):
            if (_bd[i][j] == 3 and _rd[i][j]==rd_count-1):
                sum += expand_green(_bd, _rd, rd_count, i, j)
                eval_sum +=1
            elif (_bd[i][j] == 4 and _rd[i][j]==rd_count-1):
                sum += expand_red(_bd, _rd, rd_count, i, j)
                eval_sum += 1
            elif(_bd[i][j] == 1):
                check_one+=1;
    if(sum==eval_sum or check_one==0):
        return -101;
    return 1;

class green:
    def __init__(self, greena, _temp):
        self.greena = greena;
        green_tmp = _temp[:];
        delete(green_tmp, greena)
        self.reds = list();
        self.reds = list(combinations(green_tmp, red_count));


n, m, green_count, red_count = map(int, input().split())
board = [[0 for col in range(m)] for row in range(n)]
rounds = [[0 for col in range(m)] for row in range(n)]
for i in range(n):
    board[i] = list(map(int, input().split()) )

#print_arr(board)
nutri_ables=list()

for i in range(n):
    for j in range(m):
        if(board[i][j] == 2):
            nutri_ables.append([i,j])

# 조합의 경우의 수를 구해서

temp=list()
for i in range(len(nutri_ables)):
    temp.append(i)


result =list();

comb_greens=list();
comb_greens=list(combinations(temp, green_count));


class_greens=list();
# 1이 없어질 때 까지 다 탐색 하면 된다.
for i in range(len(comb_greens)):
    _one_green=green(comb_greens[i], temp)
    class_greens.append(_one_green)
#nutri_ables
# green과 red의 조합일 경우에 맵에서 어떻게 작동되는지 확인해보자
# 0은 호수
# 1은 배양액을 뿌릴 수 없는 땅
# 2는 배양액을 뿌릴 수 있는 땅


max=-1;
import queue


def bfs_board(_bd, _rd, _gq,_rq,rd_count, g_count, r_count, v_count ):
    while( ~_gq.empty() or ~ _rq.empty() ):
        _gq.get


import copy as cp
for i in range(len(class_greens)):
    for j in range(len(class_greens[i].reds)):

        # nutri_ables 는 (a,b)의 형태
        # green 은 3
        # red 은 4
        #----------------------------
        tmp_board = cp.deepcopy(board)
        tmp_rounds = cp.deepcopy(rounds)
        round_count = 0;
        gQ=queue.Queue();
        rQ = queue.Queue();
        for _k in range(green_count):
            _comb = class_greens[i].greena[_k]
            a = nutri_ables[_comb][0]
            b = nutri_ables[_comb][1]
            tmp_board[a][b]=3;
            tmp_rounds[a][b]=0;
            gQ.put([a, b]);
        for _o in range(red_count):
            _comb= class_greens[i].reds[j][_o]
            a = nutri_ables[_comb][0]
            b = nutri_ables[_comb][1]
            tmp_board[a][b] = 4;
            tmp_rounds[a][b] = 0;
            rQ.put([a, b]);
        for _i in range(n):
            for _j in range(m):
                if (tmp_board[_i][_j] == 2):
                    tmp_board[_i][_j] = 1;

        # 다심었다 퍼트려 보자

        # while True:
        #     round_count += 1;
        #     if(change_board(tmp_board, tmp_rounds, round_count)==-101):
        #         break;
        q = queue.Queue();
        bfs_board(tmp_board, tmp_rounds, gQ, rQ, round_count
                  , green_count, red_count, len(nutri_ables)-green_count-red_count )
        # -------------------------
        tmp_sum=sum_board(tmp_board)
        if(tmp_sum>max):
            max=tmp_sum
        tmp_board.clear()
        tmp_rounds.clear()

print(max)

