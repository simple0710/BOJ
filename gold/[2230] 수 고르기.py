# 2023/07/19 TwoPointer, Sorting
# https://www.acmicpc.net/problem/2230
import sys

def two_pointer():
  s = 0
  e = 1
  res = sys.maxsize
  while e < N:
    check = data[e] - data[s]
    # 같은 인덱스인 경우, check가 M 미만인 경우
    if s == e or check < M:
      e += 1
    else: # check가 M 이상인 경우
      s += 1
      res = min(res, check)
  # 정답 출력
  print(res)

N, M = map(int,input().split())
data = sorted([int(input()) for _ in range(N)])
# 탐색 시작
two_pointer()