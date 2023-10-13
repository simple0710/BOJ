# 2023/06/22 TwoPointer, Sorting
# https://www.acmicpc.net/problem/3649
import sys
input = sys.stdin.readline

def two_pointer():
  s = 0
  e = N - 1
  while s < e:
    check = lego[s] + lego[e]
    if check <= X: # 두 레고의 합이 X보다 작거나 같은 경우
      if check == X: # X와 같은 경우
        return (f'yes {lego[s]} {lego[e]}')
      s += 1
    else: # 두 레고의 합이 X보다 큰 경우
      e -= 1
  # X와 같은 경우가 없을 경우
  return 'danger'

while True:
  try:
    X = int(input()) * 10000000
    N = int(input())
    lego = []
    for _ in range(N):
      lego.append(int(input()))
    lego.sort()
    # 탐색 시작 및 정답 출력
    print(two_pointer())
  except:
    break