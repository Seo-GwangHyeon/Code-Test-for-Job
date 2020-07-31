

def solution(budgets, M):
    answer=0
    budgets =sorted(budgets)
    L=len(budgets)
    if max(budgets) >= M:
        answer=M//L
    elif sum(budgets) <= M:
        answer = max(budgets)
    else:
        for i in range(L) :
            M -= budgets[i]
            if i < L-1 and budgets[i+1] > M // (L-i-1):
                answer=M // (L-i-1)
                break;
    return answer

print(solution([120,110,140,150],520) )

print(solution([120,110,140,150],485))

print(solution([9, 8, 5, 6, 7],13))
