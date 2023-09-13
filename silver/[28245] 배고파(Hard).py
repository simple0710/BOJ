# 2023/06/17 Bruteforcing
# https://www.acmicpc.net/problem/28245
import sys
input = sys.stdin.readline

def two_pointer(number):
  s = 0
  e = len(bin(number)) - 2
  res_s = 0
  res_e = 0
  check_total = number
  while s <= e:
    v = 2 ** s + 2 ** e
    if abs(number - v) < check_total: # 해당하는 경우를 찾는다.
      check_total = abs(number - v)
      res_s = min(s, e)
      res_e = max(s, e)
    if v <= number:
      s += 1
    else:
      e -= 1
  return res_s, res_e # x, y 반환

N = int(input())
for _ in range(N):
  M = int(input())
  # 탐색 후 정답 확인
  if M == 1 or M == 2:
    print(0, 0)
  else:
    check = two_pointer(M)
    print(*check)