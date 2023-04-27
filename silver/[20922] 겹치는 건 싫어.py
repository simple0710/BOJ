# 2023/04/27 TwoPointer
# https://www.acmicpc.net/problem/20922
from collections import defaultdict

def two_pointer():
  s = 0
  e = 0
  res = 0
  k_check = defaultdict(int)
  while e < N:
    if k_check[data[e]] + 1 <= K: # 같은 수가 K보다 작거나 같은 경우
      k_check[data[e]] += 1
      res = max(res, e - s + 1)
      e += 1
    else: # 같은 수가 K보다 커지는 경우
      k_check[data[s]] -= 1
      s += 1
  # 정답 출력
  print(res)

N, K = map(int,input().split())
data = list(map(int,input().split()))
# 탐색 시작
two_pointer()