# 2023/07/08 BinarySearch
# https://www.acmicpc.net/problem/2792
import sys
input = sys.stdin.readline

def binary_search():
  s = 1
  e = max(jewels)
  res = max(jewels)
  while s <= e:
    mid = (s + e) // 2 # mid는 보석의 개수를 의미한다.
    cnt = 0
    for i in jewels:
      if i % mid == 0: # 전부 나누어지는 경우
        cnt += i // mid
      else: # 나누어지지 않는 경우
        cnt += i // mid + 1
    if cnt <= N: # 인원 내로 분배가 가능한 경우
      res = min(res, mid)
      e = mid - 1
    else: # 인원 내로 분배가 불가능한 경우
      s = mid + 1
  # 정답 출력
  print(res)
N, M = map(int,input().split())
jewels = []
for _ in range(M):
  jewels.append(int(input()))
binary_search()