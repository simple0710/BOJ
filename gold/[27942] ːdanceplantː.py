# 2023/04/08 Implementation
# https://www.acmicpc.net/problem/27942
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def back(s, moves, u, d, l, r):
  flag, up, down, left, right = check(u, d, l, r)
  # 더 이상 움직일 수 없는 경우 sres와 res를 구한다.
  if not flag:
    global res, sres
    if sres < s:
      sres = s
      res = moves
    return
  
  m = max(up, down, left, right)
  # 현재 이동할 수 있는 방향중 최대 양분을 얻을 수 있는 곳으로 이동
  if m == up:
    back(s + up, moves+'U', u-1, d, l, r)
    return
  if m == down:
    back(s + down, moves+'D', u, d+1, l,  r)
    return
  if m == left:
    back(s + left, moves+'L', u, d, l-1, r)
    return
  if m == right:
    back(s + right, moves+'R', u, d, l, r+1)
    return

def check(u, d, l, r): # 각 방향의 양분의 합 구하기
  flag = True
  up = -1
  down = -1
  left = -1
  right = -1
  if u - 1 >= 0:
    up = sum(data[u - 1][l:r + 1])
  if d + 1 < N: 
    down = sum(data[d + 1][l:r + 1])
  if l - 1 >= 0:
    left = 0
    for i in range(u, d + 1):
      left += data[i][l - 1]
  if r + 1 < N:
    right = 0
    for i in range(u, d + 1):
      right += data[i][r + 1]
  # 전부 0 이하인 경우 flag = False
  if max(up, down, left, right) <= 0:
    flag = False
  return flag, up, down, left, right

N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]
u = N // 2 - 1
d = N // 2
l = N // 2 - 1
r = N // 2
res = ''
sres = 0
# 탐색 시작
back(sres, res, u, d, l, r)
# 정답 출력
print(sres)
print(res)