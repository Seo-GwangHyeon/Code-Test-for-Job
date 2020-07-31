import copy as cp
def solution(money):
    answer=0;
    n=len(money);
    i=0;
    q=list();
    for i in range(n):
        _money=cp.deepcopy(money);
        _answer=_money[i];
        _money[i]=-1
        _money[(i-1)%n] = -1
        _money[(i+1)%n] = -1
        q.append([_money, _answer])
    while len(q)>0:
        front=q.pop();
        _money=front[0]
        _answer = front[1]
        answer=max(answer,_answer)
        for i in range(n):
            if _money[i]>=0:
                _m = cp.deepcopy(_money);
                _a = _answer+_m[i];
                _m[i] = -1
                _m[(i - 1) % n] = -1
                _m[(i + 1) % n] = -1
                q.append([_m, _a])
    return answer

print(solution([1,2,3,1,1,2,3,1,1,2,1,
                2,3,1,1,2,3,1,1,2,1,2,
                3,1,1,2,3,1,1,2,1,2,3,
                1,1,2,3,1,1,2,1,2,3,1,
                1,2,3,1,1,2,1,2,3,1,1,
                2,3,1,1,2,1,2,3,1,1,2,
                3,1,1,2,1,2,3,1,1,2,3,
                1,1,2,1,2,3,1,1,2,3,1,
                1,2]));