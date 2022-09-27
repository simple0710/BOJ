from collections import deque

def bfs(x, y, d): # 너비 우선탐색
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  q = deque()
  q.append((x, y))
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # nx, ny가 구역 내이고, 수위가 d보다 높고, 방문하지 않았다면 수행
      if 0 <= nx < n and 0 <= ny < n and data[nx][ny] > d and visited[nx][ny] == 0:
        visited[nx][ny] = -1
        q.append((nx, ny))

n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]
result = list() # 각 결과를 담을 리스트 생성
for d in range(100): # 깊이, 100일 경우는 전부 잠기는 거나 다름 없음
  # 방문 기록 초기화
  visited = [([0] * n) for _ in range(n)] 
  area = 0 # 안전한 영역 초기화
  for i in range(n): # 세로 
    for j in range(n): # 가로
      # 수위가 높고, 방문하지 않았다면 수행한다.
      if data[i][j] > d and visited[i][j] == 0:
        visited[i][j] = -1
        area += 1 
        bfs(i, j, d)
  result.append(area)
print(max(result))