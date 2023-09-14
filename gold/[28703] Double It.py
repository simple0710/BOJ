# 2023/08/14 DataStructures, Greedy, PriotiryQueue
# https://www.acmicpc.net/problem/28703
import sys, heapq
input = sys.stdin.readline

N = int(input())
q = []
mx = 0
for v in map(int,input().split()):
  mx = max(mx, v)
  heapq.heappush(q, v)
checkmx = mx
res = checkmx - q[0]
while q[0] < mx: # 가장 작은 값이 mx보다 작은 경우
  v = heapq.heappop(q)
  # 최솟값 갱신
  res = min(res, checkmx - v)
  # 최댓값 갱신
  checkmx = max(checkmx, 2 * v)
  # 2배한 값 추가
  heapq.heappush(q, 2 * v)
print(min(checkmx - q[0], res)) # 정답 출력