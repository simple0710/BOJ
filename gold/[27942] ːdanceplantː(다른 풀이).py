# 2023/04/08 Implementation
# https://www.acmicpc.net/problem/27942
import sys, copy
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def back(s, moves, u, d, l, r):
  flag = True
  # 더 이상 움직일 수 없는 경우
  if min(u, d, l, r) < 0 or max(u, d, l, r) >= N + 1:
    flag = False
  else: # 움직일 수 있는 경우
    up, down, left, right = check(u, d, l, r)
    m = max(up, down, left, right)
  # 움직일 수 없다면 sres를 비교해 sres와, res를 구한다.
  if not flag or m <= 0:
    global res, sres
    if sres < s:
      sres = s
      res = moves
    return
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

def check(u, d, l, r): # 누적합
  up = -1
  down = -1
  left = -1
  right = -1
  if u - 2 >= 0 and l - 1 >= 0:
    up = n_data[u-1][r] - n_data[u-2][r] - n_data[u-1][l-1] + n_data[u-2][l-1]
  if d + 1 < N + 1 and l - 1 >= 0:
    down = n_data[d+1][r] - n_data[d][r] - n_data[d+1][l-1] + n_data[d][l-1]
  if l - 2 >= 0 and u - 1 >= 0:
    left = n_data[d][l-1] - n_data[d][l-2] - n_data[u-1][l-1] + n_data[u-1][l-2]
  if r + 1 < N + 1 and u - 1 >= 0:
    right = n_data[d][r+1] - n_data[d][r] - n_data[u-1][r+1] + n_data[u-1][r]
  # 각 방향의 양분의 합 반환
  return up, down, left, right

N = int(input())
data = [[0] * (N + 1)]
data.extend([[0] + list(map(int,input().split())) for _ in range(N)])
# 누적합 구해두기
n_data = copy.deepcopy(data)
for i in range(1, N+1):
  for j in range(1, N+1):
    n_data[i][j] += n_data[i-1][j]
    n_data[i][j] += n_data[i][j-1]
    n_data[i][j] -= n_data[i-1][j-1]
u = N // 2
d = N // 2 + 1
l = N // 2
r = N // 2 + 1
res = ''
sres = 0
# 탐색 시작
back(sres, res, u, d, l, r)
# 정답 출력
print(sres)
print(res)