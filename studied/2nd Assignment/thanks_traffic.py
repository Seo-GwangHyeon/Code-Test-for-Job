
import math
time_table = dict()


def duplicated(second):
    if second not in time_table.keys():
        return second
    else:
        return duplicated(second - 0.01)

def solution(lines):
    schedules=list()
    for i in range(len(lines)):
        one_line=lines[i].split()
        hhmmss=one_line[1].split(':')
        hour = float(hhmmss[0])
        min =  float(hhmmss[1])
        sec =  float(hhmmss[2])
        during_sec = float(one_line[2].split('s')[0])*1000

        end_sec=math.floor((hour*60*60+min*60+sec)*1000)
        start_sec= math.floor(end_sec-during_sec)+1-999.1
        time_table[duplicated(start_sec)] = i
        time_table[duplicated(end_sec)] = i
    history = []
    state = [0] * len(lines)  # 트래픽이 동작 중인지 현재 상태 / 초기화 다 꺼져있다.
    for time in sorted(time_table.keys()):
        index = time_table[time]
        if state[index] == 0:  # 트래픽이 시작이면 켠다.
            state[index] = 1
        elif state[index] == 1:  # 트래픽이 종료시간이면 끈다.
            state[index] = 0

        history.append(state.count(1))  # 현재 동작 중인 트래픽 개수를 센다.
        # print(index, time, state, state.count(1))

    return max(history)
lines3=[
    "2016-09-15 23:59:59.999 0.001s"
]

lines1=[
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"
]
lines2=[
    "2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"
]



print(solution(lines1))
#
print(solution(lines2))
print(solution(lines3))

