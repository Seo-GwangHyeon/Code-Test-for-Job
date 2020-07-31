# def solution(food_times, k):
#     len1 = len(food_times);
#     i=0;
#     while True:
#         if(food_times[i]>0):
#             k-=1;
#             food_times[i]-=1;
#         i = (i + 1) % len1;
#         if (k <= 0 and food_times[i]>0):
#             answer = i+1;
#             break;
#         if(max(food_times)==0):
#             answer=-1;
#             break;
#     return answer
from queue import PriorityQueue
def solution(food_times, k):
    if sum(food_times)<=k:
        return -1;

    answer = 0;
    q=PriorityQueue();
    for i in range(len(food_times)):
        q.put([food_times[i], i+1])
    sum_value=0
    previous =0
    length = len(food_times)
    while sum_value + ((q.queue[0][0]-previous)*length)<=k:
        now=q.get()[0]
        sum_value+=(now-previous)*length;
        length -=1
        previous=now
    result=sorted(q.queue, key=lambda x:x[1])
    index=(k-sum_value)%len(q.queue)
    return result[index][1]

print("answer", solution([3,1,2], 5))




