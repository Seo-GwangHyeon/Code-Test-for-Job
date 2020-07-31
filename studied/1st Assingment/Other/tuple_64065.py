
def f2(x):
    return x[1]

def solution(s):
    arr=[]
    dic=dict()
    s=s.split("{")
    for p in s:
        #print(p.split("}"))
        temp = p.split("}")
        if(temp[0]!=""):
            arr.append(temp[0])
    for a in arr:
        _arr=a.split(',')
        for k in _arr:
            dic[k] = 0
    for a in arr:
        _arr = a.split(',')

        for k in _arr:
            dic[k] += 1
    __sorted =sorted(dic.items(), key=f2, reverse=True)
    answer = []
    for a in __sorted:
        answer.append(int(a[0]))


    return answer



print(solution( "{{2},{2,1},{2,1,3},{2,1,3,4}}"))