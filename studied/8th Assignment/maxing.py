from itertools import permutations
import copy as cp

def operation(a, b, oper):
    if oper == '+':
        return a + b
    elif oper == '-':
        return a - b
    elif oper == '*':
        return a * b

def make_list(expression):
    ex_list = list()
    temp = ""
    for e in expression:
        if e == '+' or e == '*' or e == '-':
            ex_list.append(int(temp))
            ex_list.append(e)
            temp = ""
        else:
            temp += e
    ex_list.append(int(temp))
    return ex_list

def calculate(ex_list, p):
    _ex_list = cp.deepcopy(ex_list)
    for _p in p:
        i=1
        n=len(_ex_list)
        while i < n:
            if _ex_list[i] == _p:
                temp = operation(_ex_list[i-1], _ex_list[i+1], _p)
                #뒤에서 부터 지운다.
                _ex_list.remove(_ex_list[i+1])
                _ex_list.remove(_ex_list[i])
                _ex_list[i - 1] = temp
                i-=2
                n-=2
            i+=1
    return abs(_ex_list[0])

opers=['+','-','*']

def solution(expression):
    answer = 0
    ex_list=make_list(expression)
    permutes=list(permutations(opers,3))
    max1=-1
    for p in permutes:
        max1 = max(max1, calculate(ex_list, p))
    answer=max1
    return answer

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))