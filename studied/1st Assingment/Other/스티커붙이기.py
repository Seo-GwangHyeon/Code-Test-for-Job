# n 세로 행수 , m 가로 열수, sticker 수
# arr2=rotate(arr,1,2,3)
# arr3=rotate(arr,2,2,3)
# arr4=rotate(arr,3,2,3)


class sticker:
    def __init__(self, shape,n,m):
        self.shape = shape;
        self.n = n;
        self.m = m;

def rotate(_st):
    tmp_st = sticker(_st.shape,_st.n,_st.m);
    arr_result = [[0 for col in range(10)] for row in range(10)]
    for i in range(tmp_st.n):#행
        for j in range(tmp_st.m):#열
             arr_result[j][tmp_st.n-1-i]=tmp_st.shape[i][j]
    temp = tmp_st.m
    tmp_st.m = tmp_st.n
    tmp_st.n = temp
    tmp_st.shape = arr_result
    return tmp_st


class stickers:
    def __init__(self, _st):
        self.a = list();
        self.a.append(_st)
        self.a.append(rotate(_st))
        self.a.append(rotate(self.a[1]))
        self.a.append(rotate(self.a[2]))

def test_attach(a, b, _st):
    #a행 b 열는 보드 위치
    if (a+_st.n > n or b + _st.m > m):
        return False
    for i in range(_st.n):
        for j in range(_st.m):
            if( board[a+i][b+j] == 1 and _st.shape[i][j] == 1):
                return False
    return True;

def real_attach(a, b, _st):
    #a행 b 열는 보드 위치
    if (a+_st.n > n or b + _st.m > m):
        return
    for i in range(_st.n):
        for j in range(_st.m):
            if( board[a+i][b+j] == 0):
                board[a+i][b+j]=_st.shape[i][j];
    return ;

# n 세로 행수 , m 가로 열수, sticker 수
n, m, st = map(int, input().split())

board = [[0 for col in range(m)] for row in range(n)]

st_collec=list();
for k in range(st):
    a, b = map(int, input().split())
    tmp_arr = [[0 for col in range(b)] for row in range(a)]
    for i in range(a):
        tmp_arr[i]= list(map(int, input().split()))
    tmp_st=stickers(sticker(tmp_arr, a, b))
    st_collec.append(tmp_st);

for k in range(st):
    for p in range(4):
        attached=False;
        for i in range(n):
            for j in range(m):
                if( test_attach(i,j,st_collec[k].a[p]) ==True):
                    real_attach(i,j,st_collec[k].a[p])
                    attached=True;
                    break;
            if(attached):
                break;
        if (attached):
            break;

result =0;
for i in range(n):
    for j in range(m):
        result+=board[i][j];
print(result)







