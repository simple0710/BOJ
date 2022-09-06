import sys
import heapq

input = sys.stdin.readline

data = []
t = int(input())

for _ in range(t):
    x = int(input())
    if x != 0:
        # 오름차 순으로 진행한다.
        heapq.heappush(data, -x)
    else:
        # 가장 작은 값(가장 큰 값)을 제거하고 출력한다.
        if data:
            print(-heapq.heappop(data))
        # 길이가 0인 경우 0을 츨력한다.
        else:
            print(0)
