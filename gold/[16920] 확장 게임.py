# 2023//01/15 BFS
# https://www.acmicpc.net/problem/16920
from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1 ,1]

def bfs():
  flag = 1
  while flag:
    flag = 0
    for i in range(1, P+1): # 플레이어
      if not player[i]: # 이동할 공간이 없으면 스킵
        continue
      for _ in range(p_moves[i]): # 움직일 수 있는 수만큼 움직인다. 
        if not player[i]:
          break
        for _ in range(len(player[i])): # 턴
          x, y = player[i].popleft()
          for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if 0 <= nx < N and 0 <= ny < M and data[nx][ny] == '.':
              player[i].append((nx, ny))
              data[nx][ny] = i
              flag = 1
              res[i] += 1
  return

if __name__=="__main__":
  N, M, P = map(int,input().split())
  p_moves = [0] + list(map(int,input().split()))
  data = []
  player = [0] + [deque() for _ in range(P)]
  res = [0] * (P+1)
  for i in range(N):
    data.append(list(input().rstrip()))
    for j in range(M):
      if data[i][j].isdigit():
        player[int(data[i][j])].append((i, j))
        res[int(data[i][j])] += 1

  # 탐색 시작
  bfs()

  # 정답 출력
  print(' '.join(map(str, res[1:])))
