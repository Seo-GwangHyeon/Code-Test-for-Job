# string 덧셈 구현 문제이다.
# 맨처음에 값을 찾은후
# 뒤에는 점점
def gcd(a, b): # 최소 공배수
  while (b != 0):
    temp = a % b
    a = b
    b = temp
  return abs(a)

n = int(input())
min = pow(10,18)
last_remain=0
pay = None
valid =True
for i in range(n):
    imexport, remain = map(int, input().split())

    if ( imexport + last_remain  < 0):
        temp= remain -(imexport+last_remain)
        if (remain !=0 and remain < min ):
            min=remain
        if (pay == None):
            pay=temp
        else:
            pay=gcd(pay, temp)
            if( pay <= min and min != pow(10,18)):
                valid = False
                break;
    else:
        if (last_remain + imexport != remain):
            valid=False
            break;
    last_remain=remain
if (valid and pay != None ) :
    print(pay)
elif (valid and pay== None) :
    print(1)
else : print(-1)
