# sliding window + dictionary
def solution(gems):
    gem_dic=dict()
    for i in range(len(gems)):
        gem_dic[gems[i]]=list()
    kind=len(gem_dic)
    start=0
    end=0
    min1= 123456789
    wishlist=list()
    answer=[]
    check_present=True
    for i in range(len(gems)):
        if(kind>0):
            check_present = len(gem_dic[gems[i]]) > 0
        wishlist.append(gems[i])
        gem_dic[gems[i]].append(i)
        end +=1
        if len(wishlist)>1 :
            while len(gem_dic[wishlist[0]]) > 1:
                gem_dic[wishlist[0]].pop(0)
                wishlist.pop(0)
                start += 1
        if kind>0 and  not check_present:
            kind-=1
        if kind==0:
            if min1 > len(wishlist):
                min1=len(wishlist)
                answer=[start+1,end]
        if min1==len(gem_dic):
            break
    return answer

print(solution(
    ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA" , "DIA"]
))


print(solution(
    ["A","B","A","A","C","C","B","B","A","A","C","C","B","C","A","C"]
))

