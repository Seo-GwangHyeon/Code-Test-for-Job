def solution(money):
    dp1=[0]*len(money);
    dp1[0]=money[0]
    dp1[1] = max(money[0],money[1])

    #현재 집을 털 것인지 이전집을 털것인지
    for i in range(2, len(money)-1):
        dp1[i]=max(dp1[i-1], money[i]+dp1[i-2] )

    dp2=[0]*len(money)
    dp2[0]=0
    dp2[1]=money[1]

    for i in range(2, len(money)):
        dp2[i]=max(dp2[i-1], money[i]+dp2[i-2])
    return max(max(dp1), max(dp2))

solution([1,2,3,1])