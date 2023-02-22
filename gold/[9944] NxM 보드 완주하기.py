# 2023/02/22 구현
# https://www.acmicpc.net/problem/9944
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, total_cnt, cnt): # 현재 위치, 방문한 칸, 이동한 경우
  global res
  if total_cnt == all_cnt: # 모든 칸을 방문한 경우
    if res == -1 or res > cnt: # cnt가 res보다 더 작은 경우
      res = cnt
    return
  if res == -1 or cnt < res:
    for i in range(4): 
      new_visited = [] # 방문했던 장소를 저장하는 배열
      nx = x
      ny = y
      while True:
        nx += dx[i]
        ny += dy[i]
        if 0 <= nx < N and 0 <= ny < M and data[nx][ny] == '.':
          new_visited.append((nx, ny))
          data[nx][ny] = '*'
        else:
          break
      if new_visited: # 방문한 곳이 있는 경우
        dfs(nx-dx[i], ny-dy[i], total_cnt + len(new_visited), cnt+1)
        for a, b in new_visited: # 원상복구
          data[a][b] = '.'

case_cnt = 1
while True:
  try:
    N, M = map(int,input().split())
    data = []
    all_cnt = 0
    for i in range(N): # 모든 공간의 합 구하기
      data.append(list(input().rstrip()))
      all_cnt += data[i].count('.')

    res = -1
    for i in range(N):
      for j in range(M):
        if data[i][j] == '.': # 해당 위치에서 탐색 시작
          data[i][j] = '*'
          dfs(i, j, 1, 0)
          data[i][j] = '.'

    # 정답 출력
    print(f'Case {case_cnt}: {res}')
    case_cnt += 1
  except:
    break