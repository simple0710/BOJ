# 2023/03/13 Implement
# https://www.acmicpc.net/problem/15685
import sys
input = sys.stdin.readline
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def solution(data):
  y, x, d, g = data
  board[x][y] = 1
  board[x + dx[d]][y + dy[d]] = 1
  x, y = x + dx[d], y + dy[d] # 현재 위치
  total_dr = [d] # 0세대
  for _ in range(g):
    for d in total_dr[::-1]: # 끝부분부터 시작한다.
      for i in range(4):
        if d == i: # 방향 확인
          nd = (d + 1) % 4 # 시계 방향으로 90도 회전
          x += dx[nd]
          y += dy[nd]
          board[x][y] = 1
          total_dr.append(nd)

board = [[0] * 101 for _ in range(101)]
for _ in range(int(input())):
  solution(map(int,input().split()))

res = 0
for i in range(100):
  for j in range(100):
    # 해당 구역에서 정사각형을 만들 수 있는 경우
    if board[i][j] and board[i+1][j] and board[i][j+1] and board[i+1][j+1]:
        res += 1
# 정답 출력
print(res)