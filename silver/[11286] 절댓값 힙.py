import heapq
import sys

input = sys.stdin.readline

t = int(input())
data = []
for _ in range(t):
    x = int(input())
    if x != 0:
        # 절댓값을 값에 추가해 크기 순으로 분류한다.
        heapq.heappush(data, (abs(x),x))
    else:
        if data:
            print(heapq.heappop(data)[1])
        else:
            print(0)
