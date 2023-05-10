# 2023/05/10 BinarySearch
# https://www.acmicpc.net/problem/16564
import sys
input = sys.stdin.readline

def binary_search():
  s = min(data) # 최솟값
  e = K + max(data) # 최댓값
  res = min(data)
  while s <= e:
    mid = (s + e) // 2
    check = 0
    for i in data:
      if mid > i:
        check += mid - i
    if check <= K: # check가 K보다 작거나 같은 경우
      s = mid + 1
      res = max(res, mid)
    else: # check가 K보다 큰 경우
      e = mid - 1
  # 정답 출력
  print(res)

N, K = map(int,input().split())
data = []
for _ in range(N):
  data.append(int(input()))
# 탐색 시작
binary_search()