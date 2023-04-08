# 2023/04/08 BinarySearch
# https://www.acmicpc.net/problem/1072
import sys
input = sys.stdin.readline
MAX = sys.maxsize

def binary_search():
  now = int((Y * 100 // X)) # 소수점은 버림
  s = 0
  e = MAX
  res = MAX
  while s <= e:
    mid = (s + e) // 2
    check = int((Y + mid) * 100 // (X + mid))
    if now != check: # 값이 변한 경우
      res = min(res, mid)
    if check <= now:
      s = mid + 1
    else:
      e = mid - 1
  if res == MAX: # 바뀌지 않는 경우 res = -1
    res = -1
  # 정답 반환
  return res

X, Y = map(int,input().split())
# 탐색 후 정답 출력
print(binary_search())