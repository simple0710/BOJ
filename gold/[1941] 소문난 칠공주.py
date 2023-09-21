# 2023/09/21 Math, Bruteforcing, BFS, Backtracking, Combinatorics
# https://www.acmicpc.net/problem/1941
from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(arr): # 확인
  q = deque([arr[0]])
  visited = [[True] * 5 for _ in range(5)]
  for x, y in arr:
    visited[x][y] = False
  visited[arr[0][0]][arr[0][1]] = True
  cnt = 1
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
        q.append((nx, ny))
        visited[nx][ny] = True
        cnt += 1
  return cnt == 7 # 모두 연결된 경우 True 반환

def back(depth, cnt, x, y):
  global res
  if cnt >= 4: # 임도연파가 4명 이상인 경우 종료
    return
  if depth == 7: # 7명이 결성된 경우 조합 확인
    res += bfs(arr)
    return
  # 모든 경우 확인
  for i in range(x, 5):
    for j in range(y if x == i else 0, 5):
      arr.append((i, j))
      back(depth + 1, cnt + (board[i][j] == 'Y'), i, j)
      arr.pop()

def solution():
  global res, arr
  arr = []
  res = 0
  back(0, 0, 0, 0) # 탐색 시작
  return res # 정답 출력

def main():
  global board
  board = [input().rstrip() for _ in range(5)]
  print(solution()) # 정답 출력

if __name__ == "__main__":
  main()