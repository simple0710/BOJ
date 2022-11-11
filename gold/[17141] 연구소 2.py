# 2022/11/10 너비우선탐색
from collections import deque
from itertools import combinations

# 너비우선탐색
def bfs():
  res = -1
  # combinations를 이용해 바이러스가 들어갈 수 있는 항목을 모두 표시한다.
  virus = combinations(total_virus, M)
  # 바이러스 M개의 조합으로 바이러스를 퍼지게 한다.
  for i in virus:
    visited = [[False] * N for _ in range(N)]
    for x, y in i:
      visited[x][y] = True
    q = deque()
    q.extend(i)
    time = 0
    while q:
      time += 1
      for _ in range(len(q)):
        x, y = q.popleft()
        for move in range(4):
          nx = x + dx[move]
          ny = y + dy[move]
          # 벽 빼고는 다 움직여 본다.
          if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and data[nx][ny] != 1:
            q.append((nx, ny))
            visited[nx][ny] = True

    i_cnt = 0
    for i in visited:
      i_cnt += i.count(False)
    if i_cnt == wall:
      if res == -1 or res > time:
        res = time
  return res
  
if __name__ == "__main__":
  # 정보 입력
  N, M = map(int,input().split())
  data = []
  total_virus = []
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  wall = 0
  for i in range(N):
    data.append(list(map(int,input().split())))
    for j in range(N):
      # 바이러스를 둘 수 있는 위치를 저장한다.
      if data[i][j] == 2:
        total_virus.append((i, j))
      # 벽의 개수를 세어둔다.
      if data[i][j] == 1:
        wall += 1
  # 실행
  res = bfs()

  # 정답 출력
  # 모든 공간을 감염시키지 못했을 경우
  if res == -1:
    print(res)
  else:
    # res-1인 이유는 모든 칸을 채우고 나서 나머지를 소모하는 시간을 빼주는 것이다.
    print(res-1)