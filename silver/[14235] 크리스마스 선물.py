# 2023/03/31 Priority Queue
# https://www.acmicpc.net/problem/14235
import heapq

present = []
res = []
N = int(input())
for _ in range(N):
  place = list(map(int,input().split()))
  if place[0] == 0: # 아이들 거점지
    if present: # 줄 수 있는 선물이 있는 경우
      p = -heapq.heappop(present)
    else:
      p = -1
    res.append(p)
  else: # 선물이 있는 거점
    for i in place[1:]: # 선물 가져가기
      heapq.heappush(present, -i)

for i in res: # 정답 출력
  print(i)