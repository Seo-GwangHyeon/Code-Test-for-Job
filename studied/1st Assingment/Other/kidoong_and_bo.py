# x, y는 기둥, 보를 설치 또는 삭제할 교차점의 좌표이며, [가로 좌표, 세로 좌표] 형태입니다.
# a는 설치 또는 삭제할 구조물의 종류를 나타내며, 0은 기둥, 1은 보를 나타냅니다.
# b는 구조물을 설치할 지, 혹은 삭제할 지를 나타내며 0은 삭제, 1은 설치를 나타냅니다.


def solution(n, build_frame):
    answer = list()

    #print(build_frame)

    #for build in build_frame:
        #if( build[3]==-1):
            #build_frame.remove(build)
    #print(build_frame)

    for i in range(len(build_frame)):
        x=build_frame[i][0]
        y = build_frame[i][1]
        kind = build_frame[i][2]
        insdel = build_frame[i][3]
        # 2 2 에 기둥이 있으려면
        # 2,1 /  기둥이 있거나
        #
        print(answer)
        if insdel==1:
            if kind==0:
                if( y==0):
                    answer.append([x,y,kind,0])
                elif(y>0):
                    for j in range(len(answer)):
                        #print(answer)
                        inst_x = answer[j][0]
                        inst_y = answer[j][1]
                        inst_kind = answer[j][2]
                        is_below_kidoong = (inst_x==x and y-1==inst_y)
                        if inst_kind==0 and is_below_kidoong:
                            answer.append([x, y, kind, 0])
                            answer[j][3] += 1
                            break;
                        elif ( inst_kind==1 and ((inst_x==x-1 and y==inst_y)
                        and (inst_x==x and y==inst_y)   ) and x-1>=0
                               and x+1< n
                        ):
                            answer.append([x, y, kind, 0])
                            answer[j][3] += 1
                            break;
            elif kind==1:
                if (y == 0):
                    continue;
                elif (y>0 ):
                    for j in range(len(answer)):
                        inst_x = answer[j][0]
                        inst_y = answer[j][1]
                        inst_kind = answer[j][2]
                        if( inst_kind==0 and ((inst_x==x and inst_y==y-1)
                        or (inst_x==x+1 and inst_y==y-1) )
                        ):
                            answer.append([x, y, kind, 0])
                            answer[j][3]+=1
                            break;
                        elif ( inst_kind==1 and ((inst_x==x-1 and y==inst_y)
                        and (inst_x==x+1 and y==inst_y))
                                and x-1>=0 and x+1<n
                        ):
                            answer.append([x, y, kind, 0])
                            answer[j][3] += 1
                            break;



    answer = sorted(answer)
    print("answer")
    print(answer)
    return answer

print(solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))