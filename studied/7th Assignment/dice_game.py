n=10

def make_tree():
    tree = list()
    tree.append(node(0, 2))  # 0
    tree.append(node(1, 4))  # 1
    tree.append(node(2, 6))  # 2
    tree.append(node(3, 8))  # 3

    ####
    tree.append(node(4, 10))  # 4

    # ------
    tree.append(node(5, 12))  # 5
    tree.append(node(6, 14))  # 6
    tree.append(node(7, 16))  # 7
    tree.append(node(8, 18))  # 8
    ####
    tree.append(node(9, 20))  # 9
    # ------
    tree.append(node(10, 13))  # 10
    tree.append(node(11, 16))  # 11
    tree.append(node(12, 19))  # 12
    ####
    tree.append(node(13, 25))  # 13
    # ------
    tree.append(node(14, 22))  # 14
    tree.append(node(15, 24))  # 15
    # ------
    tree.append(node(16, 22))  # 16
    tree.append(node(17, 24))  # 17
    tree.append(node(18, 26))  # 18
    tree.append(node(19, 28))  # 19
    ####
    tree.append(node(20, 30))  # 20
    # ------
    tree.append(node(21, 28))  # 21
    tree.append(node(22, 27))  # 22
    tree.append(node(23, 26))  # 23
    # ------
    tree.append(node(24, 30))  # 24
    tree.append(node(25, 35))  # 25
    tree.append(node(26, 40))  # 26
    # ------
    tree.append(node(27, 32))  # 27
    tree.append(node(28, 34))  # 28
    tree.append(node(29, 36))  # 29
    tree.append(node(30, 38))  # 30

    tree.append(node(31, 0))  # 31 start
    tree.append(node(32, 0))  # 32 end

    tree[31].set_next(tree[0], -1)
    tree[0].set_next(tree[1], -1)
    tree[1].set_next(tree[2], -1)
    tree[2].set_next(tree[3], -1)
    tree[3].set_next(tree[4], -1)

    tree[3].set_next(tree[4], -1)
    tree[4].set_next(tree[5], tree[10])
    tree[5].set_next(tree[6], -1)
    tree[6].set_next(tree[7], -1)
    tree[7].set_next(tree[8], -1)
    tree[8].set_next(tree[9], -1)
    tree[9].set_next(tree[16], tree[14])
    tree[10].set_next(tree[11], -1)
    tree[11].set_next(tree[12], -1)
    tree[12].set_next(tree[13], -1)
    tree[14].set_next(tree[15], -1)
    tree[15].set_next(tree[13], -1)
    tree[16].set_next(tree[17], -1)
    tree[17].set_next(tree[18], -1)
    tree[18].set_next(tree[19], -1)
    tree[19].set_next(tree[20], -1)
    tree[20].set_next(tree[27], tree[21])
    tree[21].set_next(tree[22], -1)
    tree[22].set_next(tree[23], -1)
    tree[23].set_next(tree[13], -1)
    tree[13].set_next(tree[24], -1)
    tree[24].set_next(tree[25], -1)
    tree[25].set_next(tree[26], -1)
    tree[26].set_next(tree[32], -1)
    tree[27].set_next(tree[28], -1)
    tree[28].set_next(tree[29], -1)
    tree[29].set_next(tree[30], -1)
    tree[30].set_next(tree[26], -1)
    return tree;

class node:
    def __init__(self,idx, score):
        self.idx = idx;
        self.score=score;
        self.red_next = -1
        self.blue_next = -1
    def set_next(self, red_next, blue_next):
        self.red_next = red_next
        self.blue_next = blue_next

tree=make_tree();
dices=list(map(int, input().split(' ')  ))


# DFS 탐색
# 말은 4개
# 총 10번 주사위
# 31 start / 32 end
def move(tree, go_horse, dice):
    result = tree[go_horse] # 노드
    for i in range(dice):
        if result.idx == 32:
            break;
        if i==0 and result.blue_next != -1:
            result=result.blue_next
        else:
            result = result.red_next
    return result;
wait_horses=[31,31,31,31];
gaming_horses=list();
dice_idx=0
go_horse = wait_horses.pop()

result_node=move(tree, go_horse, dices[dice_idx]);
score=result_node.score;
gaming_horses.append(result_node.idx);

dfs=list();
import copy as cp
dfs.append([wait_horses, gaming_horses, score, dice_idx+1])
max1=0;
while(len(dfs) > 0):
    p=dfs.pop()
    _whorses = p[0]
    _ghorses = p[1]
    _score = p[2]
    _dice_idx =p[3]
    if _dice_idx>=10:
        max1=max(max1, _score)
    else:
        # 경우 1 대기말 사용
        if len(_whorses) >0:
            __whorses = cp.deepcopy(_whorses)
            __ghorses = cp.deepcopy(_ghorses)
            result_node = move(tree, __whorses.pop(), dices[_dice_idx])
            flag=True;
            for game in __ghorses:
                # 같은 칸에 2개의 말이 들어갈 수 없다.
                if game ==result_node.idx:
                    flag=False;
            if  result_node.idx==32:
                flag=True
            if flag :
                __ghorses.append(result_node.idx)
                dfs.append([__whorses, __ghorses, _score+result_node.score, _dice_idx+1 ])
        # 경우 2 진행중인 말들 사용
        for game in _ghorses:
            __whorses = cp.deepcopy(_whorses)
            __ghorses = cp.deepcopy(_ghorses)
            result_node = move(tree, game, dices[_dice_idx])
            flag = True;
            for _game in _ghorses:
                # 같은 칸에 2개의 말이 들어갈 수 없다.
                if _game == result_node.idx:
                    flag = False;
            if  result_node.idx==32:
                flag=True
            if flag:
                __ghorses.remove(game);
                __ghorses.append(result_node.idx)
                dfs.append([__whorses, __ghorses, _score+result_node.score, _dice_idx + 1])
print(max1);

