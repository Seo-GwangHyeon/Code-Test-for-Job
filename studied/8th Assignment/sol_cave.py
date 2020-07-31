# 우선순위가 존재하는 트리
def check_order(visited, current, order ):
    for i in order:
        if i[1]==current:# 뒤에 순서에 1이 있으면
            if(visited[i[0]]>=1):
                return True;
            else: # 아직 순서 만족 못함
                return False;
    return True;


def solution(n, path, order):
    tree= [list() for col in range(n)]
    visited= [0 for col in range(n)]
    cango = [0 for col in range(n)]
    before=dict()
    after = dict()

    answer = False
    for i in path:
        tree[i[0]].append(i[1])
        tree[i[1]].append(i[0])
    for o in order:
        before[o[0]]=o[1]
        after[o[1]] = o[0]
    start = 0
    stack = list()
    if after.get(0) is None:
        for i in tree[0]:
            stack.append(i)
    else:
        stack.append(start)
    while len(stack)>0:
        current = stack.pop()
        cango[current]=1
        if after.get(current) is None: #선행 조건 없음
            visited[current]=1
            for i in tree[current]:
                if visited[i]==0:
                    stack.append(i)
            # 돌아가기 위해서
            if before.get(current) is not None and cango[before[current]]:
                stack.append(before[current])
        else: #선행 조건 있음
            if visited[after.get(current)]==1:
                visited[current]=1
                for i in tree[current]:
                    if visited[i] == 0:
                        stack.append(i)

    if sum(visited)==n:
        answer=True

    return answer

print( solution(9,
                [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
                ,[[8,5],[6,7],[4,1]]))

print( solution(9,
                [[8, 1], [0, 1], [1, 2], [0, 7], [4, 7], [0, 3], [7, 5], [3, 6]]
                ,[[4,1],[5,2]]))

print( solution(9,
                [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]]
                ,[[4,1],[8,7],[6,5]]))