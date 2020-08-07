from collections import deque
def compare(a, b, index):
    if index + len(a) <= len(b):
        if b[index:index+len(a)] == a:
            return True
        else:
            return False
    return False

def solution(strs, t):
    n = len(strs)
    nt=len(t)
    dp=[123456789 for _ in range(nt+1) ]

    bfs=deque()
    index=0
    lenths=[]
    for s in strs:
        lenths.append(len(s));
    for i in range(n):
        if compare(strs[i], t, index): # 만족하면
            dp[ index+lenths[i]]=1
            bfs.appendleft([strs[i], index+lenths[i], 1])
    min1=nt+1
    while bfs.__len__()>0:
        #print(dp)
        popped=bfs.popleft()
        _str, _index, _count = popped
        if _str==t:
            min1=min(_count, min1)
        if _count > nt:
            break
        for i in range(n):
            # 모든 문자열이 같은지
            # 길이가 더작은지
            if compare(strs[i], t, _index):  # 만족하면
                if dp[_index + lenths[i]] > _count+1:
                    dp[_index +  lenths[i]] = _count+1
                    bfs.appendleft([_str+strs[i], _index + lenths[i], _count+1])
    if min1 == nt+1:
        return -1
    return min1

print(solution(["ba","na","n","a"], "banana"))
print(solution(["app","ap","p","l","e","ple","pp"],"apple" ))
print(solution(["ba","an","nan","ban","n"], "banana"))