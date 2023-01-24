# 2023/01/24 두 포인터
# https://www.acmicpc.net/problem/2470
import sys
input = sys.stdin.readline

def search(): # Binary_Search
  MAX = sys.maxsize
  s = 0
  e = len(arr) - 1
  while s < e:
    temp = arr[s] + arr[e]
    if abs(temp) <= MAX:
      res = [arr[s], arr[e]]
      MAX = abs(temp)
    if temp < 0: # 0보다 작으면 s += 1
      s += 1
    else: # 0보다 크면 e -= 1
      e -= 1
  # 정답 반환
  return res

N = int(input())
arr = sorted(list(map(int,input().split())))
# 정답 출력
print(*search())