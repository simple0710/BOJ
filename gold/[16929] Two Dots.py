# 2023/12/13 DFS
# https://www.acmicpc.net/problem/16929
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_cycle(color, now):
  global res
  x, y = now
  if graph[x][y] == color: # 맨 처음 선택한 공의 색과 같은 경우 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < M:
        # 시작 지점이고 바로 옆이 아닌 경우, 정답 갱신
        if start == (nx, ny) and (visited[x][y] - visited[nx][ny]) != 1:
          res = "Yes"
        # 다음 색이 처음 선택한 공과 같고 아직 확인하지 않았다면 다음 경우 확인 
        elif color == graph[nx][ny] and not visited[nx][ny]:
          visited[nx][ny] = visited[x][y] + 1
          find_cycle(color, (nx, ny))

def solution():
  global visited, res, start
  res = "No"
  # 모든 구역 확인
  for i in range(N):
    for j in range(M):
      visited = [[False] * M for _ in range(N)]
      # 시작 지점
      visited[i][j] = 1
      start = (i, j)
      # 사이클 찾기 시작
      find_cycle(graph[i][j], (i, j))
  return res # 사이클 존재 여부 반환

def main():
  global N, M, graph
  N, M = map(int,input().split())
  graph = [list(input()) for _ in range(N)]
  print(solution()) # 사이클 존재 여부 출력

if __name__ == "__main__":
  main()