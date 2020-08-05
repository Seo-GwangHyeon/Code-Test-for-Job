from collections import deque
def compare(a, b, index):
    if index + len(a) <= len(b):
        for i in range(len(a)):
            if a[i] != b[index+i]:
                return False
        return True
    return False

import copy as cp
def solution(strs, t):
    answer = 0
    length=len(strs)
    # bfs로 탐색
    bfs=deque()
    index=0
    for s in strs:
        # 모든 문자열이 같은지
        # 길이가 더작은지
        if compare(s, t, index): # 만족하면
            result=""
            bfs.appendleft([s, index+len(s), 1])
    min1=len(t)+1
    while len(bfs)>0:
        popped=bfs.popleft()
        _str, _index, _count = popped
        if _str==t:
            min1=min(_count, min1)
        if _count > len(t):
            break
        for s in strs:
            # 모든 문자열이 같은지
            # 길이가 더작은지
            if compare(s, t, _index):  # 만족하면
                bfs.appendleft([_str+s, _index + len(s), _count+1])
    if min1 == len(t)+1:
        return -1
    return min1

print(solution(["a","b","c","a","b","c","a","b","c","a","b","c"], "abcdeeeeaavadsafasdfsdfvsdcacesasdcass"   ))
print(solution(["app","ap","p","l","e","ple","pp"],"apple" ))
print(solution(["ba","an","nan","ban","n"], "banana"))