import sys
import heapq

input = sys.stdin.readline

data = []
t = int(input())

for _ in range(t):
    x = int(input())
    if x != 0:
        heapq.heappush(data, -x)
    else:
        if data:
            # 최소 값을 제거하고 출력한다.
            print(heapq.heappop(data))
        else:
            # 길이가 0인 경우 0을 출력한다
            print(0)
