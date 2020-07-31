import sys
sys.setrecursionlimit((10**6))

class Tree:
    def __init__(self, dataList):
        self.data=max(dataList, key=lambda x:x[1] );
        #가장 큰 값을 root로 하여

        # lambda 함수 x가 입력 : 다음이 출력
        # 루트 값 보다 작으면 left List
        leftList=list(filter(lambda x:x[0] < self.data[0], dataList))
        # 루트 값 보다 크면 right List
        rightList = list(filter(lambda x:x[0] > self.data[0], dataList))

        if leftList!=[]:
            self.left=Tree(leftList)
        else:
            self.left=None;
        if rightList!=[]:
            self.right=Tree(rightList);
        else:
            self.right=None

def travel(node, postList, preList):
    postList.append(node.data)
    if node.left is not None:
        travel(node.left, postList, preList);
    if node.right is not None:
        travel(node.right, postList, preList)
    preList.append(node.data);

def solution(nodeinfo):
    answer=[]
    root= Tree(nodeinfo)
    postList=[]
    preList=[]
    travel(root, postList, preList)

    answer.append(list(map(lambda x: nodeinfo.index(x) + 1, postList)))
    answer.append(list(map(lambda x: nodeinfo.index(x) + 1, preList)))
    return answer

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))