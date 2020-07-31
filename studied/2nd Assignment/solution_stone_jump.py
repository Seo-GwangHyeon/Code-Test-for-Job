



def solution(stones, k):
    answer = 0
    _max=max(stones)
    _min=0

    while _max >= _min:
        mid=(_min+_max)//2
        zeros=0
        arr=[]
        max_zero=zeros

        for i in range(len(stones)):
            if stones[i] >= mid:
                arr.append(stones[i])
            elif stones[i] < mid:
                arr.append(0)
            if arr[i]==0:
                zeros+=1
            elif arr[i]!=0:
                max_zero = max(zeros, max_zero)
                zeros = 0
        max_zero=max(zeros, max_zero)
        if max_zero>=k:
            _max=mid-1;
        else :
            answer = mid
            _min=mid +1

    return answer



list = [100000000000000000 for i in range(200*1000)]

print(solution(list, 20));