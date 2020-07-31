class time:
    def __init__(self, hour,min):
        self.hour=hour
        self.min = min
# 9시 부턴 t분 간격으로 n번 운행하고 m명 이 탈 수 있다.
def plus_min(_time, t):
    if( (_time.min+t) //60  ==0 ):
        _time.min+= t
        return _time;
    elif ( (_time.min+t) //60 ==1 ):
        _time.min = _time.min+t-60
        _time.hour += 1
        return _time;

def minus_min(_time):
    if( _time.min-1 >=0):
        _time.min-= 1
        return _time;
    elif ( _time.min-1 <0):
        _time.min = 59
        if(_time.hour-1 <0):
            _time.hour=23;
        else:
            _time.hour -= 1
        return _time;

def is_full(n,t,m,time_list):
    now_time=time(9,0)
    temp_m=m;
    cr_count=len(time_list)
    last_time=time(0,0)
    for _time in time_list:
        if temp_m>0 and (_time.hour<=now_time.hour
                    and  _time.min<=now_time.min)   :
            # 버스 타는 크루
            temp_m-=1
            cr_count-=1;
            last_time=_time
        if (temp_m==0 or _time.hour > now_time.hour
                or ( _time.hour == now_time.hour
            and _time.min>now_time.min) ) :
            # 다음 버스 온다.
            now_time = plus_min(now_time, t);
            n-=1
            temp_m=m;
        if(n<=0):
            break;

    if(cr_count>0):
        last_time.hour = -100
        last_time.hour = -100
    else:
        last_time = minus_min(last_time);
    return last_time


def solution(n, t, m, timetable):
    answer = ''
    #자리가 꽉차는 지 여부를 체크한다.
    time_list= list()
    for a in timetable:
        temp=time(int(a[0:2]),int(a[3:5]))
        time_list.append(temp);
    time_list=list(sorted(time_list, key=lambda time: (time.hour, time.min) ))
    answer_time=is_full(n,t,m,time_list);
    # 가득 찰 때
    if answer_time.hour!=-100:
        return str(answer_time.hour).zfill(2)+":"+str(answer_time.min).zfill(2)
    else:
        now_time=time(9,0);
        for i in range(n-1):
            now_time=plus_min(now_time,t);
        answer_time=now_time;
        return str(answer_time.hour).zfill(2) + ":" + str(answer_time.min).zfill(2)
    # 가득 차지 않을때


    return answer


print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))