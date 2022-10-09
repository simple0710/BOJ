from collections import deque
import copy

# 너비 우선 탐색
def bfs(x, y):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  result = 0
  n_data[x][y] = 0

  q = deque()
  q.append((x, y))
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 범위 내, 육지인 경우, 방문하지 않은 경우를 만족하는 경우 수행
      if 0 <= nx < h and 0 <= ny < w and n_data[nx][ny] == "L" and not visited[nx][ny]:
        n_data[nx][ny] = n_data[x][y] + 1
        # 최대 값을 구함
        result = max(n_data[nx][ny], result)
        visited[nx][ny] = True
        q.append((nx, ny))
  return result

h, w = map(int,input().split())
data = [list(input()) for _ in range(h)]

answer = 0
# 전 지역 탐색
for i in range(h):
  for j in range(w):
    # 육지인 경우
    if data[i][j] == 'L':
      # copy할 필요 없이 visited 리스트를 이용해도 된다.
      n_data = copy.deepcopy(data)
      visited = [[False] * w for _ in range(h)]
      answer = max(answer, bfs(i,j))

print(answer)