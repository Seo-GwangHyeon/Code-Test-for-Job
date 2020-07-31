import sys

def gcd(a, b): # 최소 공배수
  while (b != 0):
    temp = a % b
    a = b
    b = temp
  return abs(a)

n = int(input())
last_remain=0;
min = pow(10,18);
pay = None
valid = True
for i in range(n):
    imexport, remain = map(int, sys.stdin.readline().split())
    # sys.stdin 이거 때문에 백준에서 시간초과 발생
    if( imexport + last_remain < 0 ):
        diff= remain - imexport - last_remain
        if(remain !=0 and remain <min):
            min=remain
        if(pay == None):# 초기에는 그냥 넘어간다.
            pay = diff;
        else:
            pay=gcd(pay, diff);
            if(pay <= min and min != pow(10,18)):
                valid =False
                break;
    else:
        if ( imexport + last_remain != remain):
            valid =False
            break;
    last_remain = remain
if (valid and pay != None ) :
    print(pay)
elif (valid and pay== None) : # 전체가 입금이면 1 출력
    print(1)
else : print(-1)