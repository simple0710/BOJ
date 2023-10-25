# 2023/06/19 Math, BinarySearch
# https://www.acmicpc.net/problem/11561
import sys
input = sys.stdin.readline

def binary_search(n):
  s = 1
  e = n
  res = 1
  while s <= e:
    mid = (s + e) // 2
    check = (mid * (mid + 1)) // 2
    if check > n: # N을 지나친 경우
      e = mid - 1
    else: # N에 도착하기 직전인 경우
      res = max(res, mid)
      s = mid + 1
  # 정답 출력
  print(res)

for _ in range(int(input())):
  # 탐색 시작
  binary_search(int(input()))