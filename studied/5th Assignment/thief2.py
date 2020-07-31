import copy as cp

def recur1(money,n,s):
    if n <= 2:
        return max(money[s:s + n]);
    if n%2==1:
        return recur1(money, n//2, s)+ recur1(money, n//2,s+n//2+1 )
    else:
        return recur1(money, n//2-1, s)+ recur1(money, n//2,s+n//2 )

def recur2(money,n,s):
    if n <= 2:
        return max(money[s:s + n]);
    if n%2==1:
        return recur2(money, n//2, s)+ recur2(money, n//2, s+n//2+1 )
    else:
        return recur2(money, n//2, s)+ recur2(money, n//2-1, s+n//2+1 )

def solution(money):
    answer=0;
    n=len(money);
    answer=max(recur1(money,n,0), recur2(money,n,0));

    return answer
print(solution([1,2,3,1]));