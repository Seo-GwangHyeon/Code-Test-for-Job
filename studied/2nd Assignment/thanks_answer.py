time_table = dict()


def duplicated(second):
    if second not in time_table.keys():
        return second
    else:
        return duplicated(second - 0.000001)


def solution(lines):
    for index, line in enumerate(lines):
        date, time, duration = line.split()  # 공백으로 분리
        h, m, n = time.split(':')  # : 시, 분, 초 분리
        end = int(h) * 60 * 60 + int(m) * 60 + float(n)  # 초로 계산
        duration = float(duration[:-1])  # 뒤에 s 제거
        start = end - duration + 0.001 - 0.9991
        time_table[duplicated(start)] = index
        time_table[duplicated(end)] = index

    history = []
    state = [0] * len(lines)  # 트래픽이 동작 중인지 현재 상태 / 초기화 다 꺼져있다.
    print( time_table)
    for time in sorted(time_table.keys()):
        index = time_table[time]
        if state[index] == 0:  # 트래픽이 시작이면 켠다.
            state[index] = 1
        elif state[index] == 1:  # 트래픽이 종료시간이면 끈다.
            state[index] = 0

        print(state);
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