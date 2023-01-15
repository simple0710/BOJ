# 2023/01/14 BFS
# https://www.acmicpc.net/problem/9328
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  q = deque()
  q.append((0, 0))
  visited = [[False] * (W + 2) for _ in range(H + 2)]
  visited[0][0] = True
  res = 0
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < (H + 2) and 0 <= ny < (W + 2) and not visited[nx][ny] and data[nx][ny] != '*':
        if 'A' <= data[nx][ny] <= 'Z': # 알파벳 대문자인 경우
          if chr(ord(data[nx][ny]) + 32) not in key:
            continue
        else:
          if 'a' <= data[nx][ny] <= 'z': # 알파벳 소문자인 경우
            if data[nx][ny] not in key:
              key[data[nx][ny]] = True
              visited = [[False] * (W + 2) for _ in range(H + 2)]
          elif data[nx][ny] == '$': # 중요 문서인 경우
            res += 1
            data[nx][ny] = '.'
        q.append((nx, ny))
        visited[nx][ny] = True
  # 정답 반환
  return res

for _ in range(int(input())):
  H, W = map(int,input().split())
  # 외곽 지점과 데이터 설정
  data = [['.'] * (W+2)]
  for i in range(H):
    data.append(list('.' + input().rstrip() + '.'))
  data.append(['.'] * (W+2))

  # 주어진 키
  key = {}
  for i in input().rstrip():
    key[i] = True
  # 탐색 및 정답 출력
  print(bfs())