# 2023/01/02 비트마스킹
# https://www.acmicpc.net/problem/14391
import sys
input = sys.stdin.readline

def dfs(sx, sy, depth):
  # 전 범위를 탐색한 경우
  if depth == (N*M):
    global res
    p = 0
    # 가로 부분을 확인한다. (True)
    for i in range(N):
      number = ''
      for j in range(M):
        if visited[i][j]:
          number += str(data[i][j])
        else:
          if number:
            p += int(number)
            number = ''
      if number:
        p += int(number)
    # 세로 부분을 확인한다. (False)   
    for j in range(M):
      number = ''
      for i in range(N):
        if not visited[i][j]:
          number += str(data[i][j])
        else:
          if number:
            p += int(number)
            number = ''
      if number:
        p += int(number)
    res = max(res, p)
    return
          
  for i in range(sx, N):
    for j in range(sy if i == sx else 0, M):
      if visited[i][j] == -1:
        visited[i][j] = True
        dfs(i, j, depth+1)
        visited[i][j] = False
        dfs(i, j, depth+1)
        visited[i][j] = -1

if __name__=="__main__":
  N, M = map(int,input().split())
  visited = [[-1] * M for _ in range(N)]
  data = [list(input()) for _ in range(N)]
  res = 0
  
  # 탐색 시작
  dfs(0, 0, 0)

  # 정답 출력
  print(res)