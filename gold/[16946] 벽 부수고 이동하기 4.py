# 2022/11/21 BFS
from collections import deque
import sys
input = sys.stdin.readline

# 방문 및 그룹 분류를 수행하는 함수
def bfs(x, y):
  q = deque()
  q.append((x, y))
  visited[x][y] = True
  cnt = 1
  while q:
    x, y = q.popleft()
    group_check[x][y] = group # 그룹 분류
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and data[nx][ny] == 0:
        q.append((nx, ny))
        visited[nx][ny] = True
        cnt += 1
  # 0의 개수 반환
  return cnt

# 정보 입력
N, M = map(int,input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
data = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[False] * M for _ in range(N)] # 방문 기록
group_check = [[0] * M for _ in range(N)] # 그룹 기록
group_dict = {} # 해당 그룹을 key로, 0의 개수를 value로 추가
group_dict[0] = 0
group = 1
for i in range(N):
  for j in range(M):
    # 0의 개수를 센 뒤 group에 추가
    if data[i][j] == 0 and not visited[i][j]:
      cnt = bfs(i, j)
      group_dict[group] = cnt
      group += 1

# 벽 주위에 그룹을 set_list에 추가한다.
for i in range(N):
  for j in range(M):
    set_list = set()
    if data[i][j]:
      for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
          set_list.add(group_check[nx][ny])
      # data[i][j]에 값을 더한뒤 10으로 나눈다.
      for k in set_list:
        data[i][j] += group_dict[k]
        data[i][j] %= 10

# 정답 출력
for i in data:
  print("".join(map(str, i)))