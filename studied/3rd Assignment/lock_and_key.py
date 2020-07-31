

def evaluate(lock):
    for l in lock:
        for k in l:
            if k != 1:
                return False;
    return True;

import copy as cp

def try_open(i, j, key,lock,M,N ):
    #i j 는 시작점
    # a, b는 블럭 크기
    # lock과 key 비교
    _lock = cp.deepcopy(lock)

    for _i in range(i, i+M+1 ):
        for _j in range(j, i+M+1):
            if _i>=0 and _i<N and _j>=0 and _j<N \
                    and _i - i>=0 and _i - i<M \
                    and _j - j>=0 and _j - j<M  :
                if _lock[_i][_j] + key[_i - i][_j - j] != 1:
                    return False;
                _lock[_i][_j] += key[_i-i][_j-j]
    if (evaluate(_lock)):
        del _lock
        return True;

def try_small_part(key, lock,M,N ):
    #시작점 지정
    for i in range(-M,N+M+1):
        for j in range(-M, N+M+1):
            is_true = try_open(i,j,key,lock,M,N);
            if is_true:
                return True;
    return False;


def rotate_ninety(lock, N):
    new_lock = [[0 for col in range(N)] for row in range(N)]
    for i in range(N):  # 행
        for j in range(N):  # 열
            new_lock[j][N - 1 - i] = lock[i][j]
    return new_lock

def solution(key, lock):
    M = len(key)
    N = len(lock)

    keys=list()
    keys.append(key)
    keys.append(cp.deepcopy(rotate_ninety(keys[0],M)))
    keys.append(cp.deepcopy(rotate_ninety(keys[1],M)))
    keys.append(cp.deepcopy(rotate_ninety(keys[2],M)))
    locks = list()
    locks.append(lock)
    locks.append(cp.deepcopy(rotate_ninety(locks[0], N)))
    locks.append(cp.deepcopy(rotate_ninety(locks[1], N)))
    locks.append(cp.deepcopy(rotate_ninety(locks[2], N)))
    for i in range(4):
        for j in range(4):
            if try_small_part(keys[j], locks[i], M, N):
                return True;
    return False;


print( solution( [ [0, 0, 1],
                   [0, 1, 0],
                   [1, 0, 1]],
               [[1, 1, 1, 0],
                [1, 1, 0, 1],
                [1, 1, 1, 1],
                [1, 1, 1, 1]]))

