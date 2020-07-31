

def check(result):
    for x, y,kind in result:
        if kind==0: #기둥 일때
            if y==0 or (x-1, y, 1) in result \
                or (x,y,1) in result or (x,y-1,0) in result:
                continue;
            else:
                return False;
        elif kind==1: # 보 일때
            if (x,y-1,0) in result or (x+1, y-1, 0) in result or \
                    ((x-1, y,1) in result and (x+1,y,1 in result)):
                continue;
            else:
                return False;
    return True;

def solution(n, build_frame):
    result=set();
    for a in build_frame:
        x, y, kind, insdel = a

        if insdel ==1:
            result.add((x, y, kind))
            is_true = check(result)
            if is_true:
                continue
            else:
                result.remove((x, y, kind))
        elif insdel ==0:
            if (x,y,kind) in result:
                result.remove((x, y, kind))
                is_true=check(result)
                if is_true:
                    continue
                else:
                    result.add((x, y, kind))
    result = [list(i) for i in result]
    return sorted(result, key=lambda x: (x[0],x[1],x[2]) )


print(solution(5,
               [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]] )
      )

print(solution(5,
               [[0,0,0,1],
                [2,0,0,1],
                [4,0,0,1],
                [0,1,1,1],
                [1,1,1,1],
                [2,1,1,1],
                [3,1,1,1],
                [2,0,0,0],
                [1,1,1,0],
                [2,2,0,1],
                [2,1,0,1],
                [2,1,0,0]]))
print(solution(5,
               [[0,0,0,1],[0,0,0,0] ] ))
