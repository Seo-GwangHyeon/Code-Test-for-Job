

ZERO=200000001

def solution(stones, k):
    answer = 0
    min_stones=min(stones)
    if(min_stones>=1):
        answer+=min_stones
        for i in range(len(stones)):
            stones[i]-=min_stones
            if(stones[i]==0):
                stones[i]= ZERO
    max_zero=-100
    while True:
        zeros=0
        for i in range(len(stones)):
            if(stones[i]==ZERO):
                zeros+=1
            else:
                zeros = 0
            if (zeros > max_zero):
                max_zero= zeros
            if (max_zero >= k):
                return answer;
        else:
            min_stones = min(stones)
            if (min_stones >= 1):
                answer += min_stones
                for i in range(len(stones)):
                    if (stones[i] < ZERO):
                        stones[i] -= min_stones
                        if (stones[i] == 0):
                            stones[i] = ZERO
    return answer



list = [100000000000000000 for i in range(200*1000)]

print(solution(list, 20));