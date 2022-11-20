# 2022/11/17 BFS, 0-1 너비 우선 탐색
'''
죄수가 탈출하는 경우
1. 두 죄수가 서로 독립된 경로로 빠져나가는 경우
2. 두 죄수 중 한 죄수가 다른 죄수 위치로 이동하고, 둘이 같이 빠져나가는 경우
3. 두 죄수가 이동하다가 중간에서 만나서 같이 빠져나가는 경우
3의 경우는 중간에서 만나는 위치가 중요하다.
'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
  # 열어야 하는 문의 개수를 구하기 위한 visited
  visited = [[-1] * (M + 2) for _ in range(N + 2)]
  q = deque()
  q.append((x, y))
  visited[x][y] = 0
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N + 2 and 0 <= ny < M + 2:
        # 아직 방문하지 않은 경우
        if visited[nx][ny] == -1:
          # 빈공간인 경우 먼저 수행
          if prison[nx][ny] == '.':
            visited[nx][ny] = visited[x][y]
            q.appendleft((nx, ny))
          # 벽인 경우 visited[x][y] + 1
          elif prison[nx][ny] == '#':
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))
  # 문을 연 횟수를 기록한 리스트 반환
  return visited

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(int(input())):
  N, M = map(int,input().split())

  # 외곽 지역을 포함해 감옥을 구현한다.
  prison = [list('.' * (M + 2))]
  for i in range(N):
    prison.append(list('.' + input().strip() + '.'))
  prison.append(list('.' * (M + 2)))

  # 사람의 위치를 저장한다.
  person = []
  for i in range(N + 2):
    for j in range(M + 2):
      if prison[i][j] == '$':
        person.append((i, j))
        prison[i][j] = '.'
  
  # 탐색 시작
  check_1 = bfs(person[0][0], person[0][1]) # 첫번째 사람
  check_2 = bfs(person[1][0], person[1][1]) # 두번째 사람
  sang = bfs(0, 0) # 제 3자, 외부에서 들어올 경우

  ans = int(1e9)
  for i in range(N + 2):
    for j in range(M + 2):
      if check_1[i][j] != -1 and check_2 != -1 and sang[i][j] != -1:
        # 해당 위치에서 문을 여는 개수
        res = check_1[i][j] + check_2[i][j] + sang[i][j]
        if prison[i][j] == "*": # 벽은 제외한다.
          continue
        # 문은 한명만 열어도 되기 때문에 나머지 사람이 연 개수인 2를 빼줌
        if prison[i][j] == '#':
          res -= 2
        ans = min(ans, res)
  # 정답 출력
  print(ans)