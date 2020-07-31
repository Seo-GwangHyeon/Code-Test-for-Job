import sys
sys.setrecursionlimit(300000)

import copy as cp
maxes=dict()
def recur(left, right):
    global maxes
    L=len(left)
    R = len(right)
    if L<=0 or R<=0:
        return 0;
    #print(maxes.get(L, R))
    if (L,R) in maxes:
        return maxes[L,R]

    lis=list()
    left1=cp.deepcopy(left)
    right1 = cp.deepcopy(right)
    left1.pop()
    a=recur(left1,right1)
    if (L,R) in maxes:
        maxes[L, R]=max(a, maxes[L, R])
    else:
        maxes[L, R]=a
    lis.append(a)

    left2 = cp.deepcopy(left)
    right2 = cp.deepcopy(right)
    left2.pop()
    right2.pop()
    b = recur(left2, right2)
    if (L,R) in maxes:
        maxes[L, R] = max(b, maxes[L, R])
    else:
        maxes[L, R] = b
    lis.append(b)

    if(left[0] > right[0]):
        left3 = cp.deepcopy(left)
        right3 = cp.deepcopy(right)
        c = right3.pop() + recur(left3, right3);
        if (L,R) in maxes:
            maxes[L, R] = max(c, maxes[L, R])
        else:
            maxes[L, R] = c
        lis.append(c)
    max1=max(lis)
    if (L,R) in maxes:
        maxes[L, R] = max(max1, maxes[L, R])
    else:
        maxes[L, R] = max1
    return max1

def solution(left, right):
    answer = 0
    n=len(left)
    answer=recur(left, right)

    return answer


# print(solution([3,2,5],[2,4,1]))

print(solution([3,2,5,1,2,3,3,1,3,4,3,2,5,1,2,3,3,1,3,4,3,2,5,1,2,3,3,1,3,4,3,2,5,1,2,3,3,1,3,4,3,2,5,1,2,3,3,1,3,4,3,2,5,1,2,3,3,1,3,4,3,2,5,1,2,3,3,1,3,4,3,2,5,1,2,3,3,1,3,4,3,2,5,1,2,3,3,1,3,4,3,2,5,1,2,3,3,1,3,4],
                [3,2,5,1,2,3,3,1,3,4,3,2,5,1,2,3,3,1,3,4,3,2,5,1,2,3,3,1,3,4,3,2,5,1,2,3,3,1,3,4,3,2,5,1,2,3,3,1,3,4,3,2,5,1,2,3,3,1,3,4,3,2,5,1,2,3,3,1,3,4,3,2,5,1,2,3,3,1,3,4,3,2,5,1,2,3,3,1,3,4,3,2,5,1,2,3,3,1,3,4]))