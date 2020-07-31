



def solution(board, moves):
    depth =len(board)
    arr=[]
    answer=0
    for move in moves:
        for i in range(depth):
            if board[i][move-1]>0:
                arr.append(board[i][move-1]);
                board[i][move - 1]=0
                if len(arr)>=2 :
                    if arr[len(arr)-2]==arr[len(arr)-1]:
                        arr.pop()
                        arr.pop()
                        answer += 2;
                break;
    return answer


print(solution(
    [[0,0,0,0,0],
     [0,0,1,0,3],
     [0,2,5,0,1],
     [4,2,4,4,2],
     [3,5,1,3,1]],
[1,5,3,5,1,2,1,4] ))

