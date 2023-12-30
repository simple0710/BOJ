# 2023/12/30 Bruteforcing, Backtracking, DFS
# https://www.acmicpc.net/problem/1189
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, distance):
  global res
  # 집에 도착했고, 거리가 K인 경우 res + 1을 한다.
  if (x, y) == (0, C-1) and distance == K:
    res += 1
    return
  # 현재 위치 방문 처리
  data[x][y] = 'T'
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < R and 0 <= ny < C and data[nx][ny] != 'T':
      data[nx][ny] = 'T' # 방문 처리
      dfs(nx, ny, distance+1) # 다음 구역 탐색
      data[nx][ny] = '.' # 방문 처리 취소

def solution():
  global res
  res = 0
  dfs(R-1, 0, 1) # 탐색 시작
  return res # 거리가 K인 가짓수 반환

def main():
  global R, C, K, data
  R, C, K = map(int,input().split())
  data = [list(input()) for _ in range(R)]
  print(solution()) # 거리가 K인 가짓수 출력

if __name__ == "__main__":
  main()