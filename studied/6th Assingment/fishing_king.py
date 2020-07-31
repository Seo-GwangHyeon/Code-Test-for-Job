class shark:
    def __init__(self, s=-1, d=-1, z=-1, r=0):
        self.spe = s
        self.dir = d-1
        self.siz = z
        if s==-1:
            self.round = -1
        else:
            self.round = r
    def re_init(self):
        self.spe = -1
        self.dir = -1
        self.siz = -1
        self.round = 0
def do_fishing(aqua, i, r, path, round):
    result=0;
    for j in range(r):
        if aqua[j][i].round == round-1:
            result = aqua[j][i].siz
            aqua[j][i]=shark();
            # print(" catch ", result)
            path[j,i].re_init()
            return result;
    return result;

def sw_dir(dir):
    if (dir == 0):
        return 1
    elif (dir == 1):
        return 0
    elif (dir == 2):
        return 3
    elif (dir == 3):
        return 2
dx = [-1,1,0,0]
dy = [0,0,1,-1]
def set_loc(x, y, r, c, dir, speed):
    global dx,dy;
    if( dir ==0 or dir==1 ): #위아래
        speed=speed%((r-1)*2)
        mx = x + dx[dir] * speed
        if mx<0 or  mx >= r:
            if mx <0 :
                mx=abs(mx);
            if(mx //(r-1))%2 ==0:
                dir = 1
                mx= 0+(mx%(r-1))
            else:
                dir = 0
                mx = (r-1) - (mx % (r - 1))
        x=mx
    elif (dir == 2 or dir == 3):
        speed = speed % ((c - 1) * 2)
        my = y + dy[dir] * speed
        if my < 0 or my >= c:
            if my < 0:
                my = abs(my);
            if (my // (c - 1)) % 2 == 0:
                dir = 2
                my = 0 + (my % (c - 1))
            else:
                dir = 3
                my = (c - 1) - (my % (c - 1))
        y=my
    return [x,y,dir]


def mov_sharks(aqua,r,c, path, round):
    global dx, dy
    _path=dict()
    for p in path.keys():
        row = p[0]
        col = p[1]
        dir = path[p].dir
        speed = path[p].spe
        size = path[p].siz
        if path[p].dir!=-1:
            if aqua[row][col].round != round:
                aqua[row][col] = shark();
            _loc=set_loc(row, col,r,c, dir,speed);

            mx = _loc[0]
            my = _loc[1]
            dir= _loc[2]
            # 상어 위치 시키기
            if(aqua[mx][my].round < round):
                new_shark=shark(speed, dir+1, size, round);
                aqua[mx][my]= new_shark;
                _path[mx, my] = new_shark;
            else : # 이번 라운드의 상어가 있는 경우
                if(aqua[mx][my].siz < size): #현재가 더 크면 먹는다. # 아니면 먹혀서 소멸
                    new_shark = shark(speed, dir+1, size, round);
                    aqua[mx][my]=new_shark
                    _path[mx, my] = new_shark;

    del(path)
    return _path;

def print_aqua(aqua, r, c):
    for i in range(r):
        for j in range(c):
            if aqua[i][j].spe==-1:
                print('0', end=' ')
            elif aqua[i][j].spe==0:
                print('O', end=' ')
            else:
                print(aqua[i][j].spe, end=' ')
        print()
    print()

r, c, m = map(int, input().split())
temp_w=shark();
aqua=[[temp_w for col in range(c)] for row in range(r)]

path=dict()
for i in range(m):
    _r, _c, _s, _d, _z = map(int, input().split())
    new_shark=shark(_s,_d,_z,0)
    aqua[_r-1][_c-1]=new_shark;
    path[_r-1, _c-1]= new_shark

result=0
for i in range(0,c):
    # 아저씨가 낚시를 한다.
    result += do_fishing(aqua, i, r, path, i+1)
    path=mov_sharks(aqua,r,c, path,i+1)

print(result)
