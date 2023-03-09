# 2023/03/09 우선순위 큐(heapq)
# https://www.acmicpc.net/problem/1202
import sys, heapq
input = sys.stdin.readline

N, K = map(int,input().split())
# 보석 정보 입력
jewels = []
for _ in range(N):
  M, V = map(int,input().split())
  heapq.heappush(jewels, (M, V))

# 가방 정보 입력
bags = []
for _ in range(K):
  bags.append(int(input()))
bags.sort()

res = 0
tmp = []
for bag in bags:
  # 가방 크기에 맞는 보석을 담아본다.
  while jewels and bag >= jewels[0][0]:
    heapq.heappush(tmp, -heapq.heappop(jewels)[1])
  if tmp: # 가장 높은 가치의 값 추가
    res -= heapq.heappop(tmp)
  elif not jewels: # 남은 보석이 없는 경우 종료
    break

# 정답 출력
print(res)