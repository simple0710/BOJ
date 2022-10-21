from collections import deque

# 너비우선탐색
def bfs(x, y):
  q = deque()
  q.append((x, y))
  visited = [False] * n
  while q:
    x, y = q.popleft()
    # 도착 지점으로 갈 수 있는 경우 happy 출력
    if (abs(x - finish_x) + abs(y - finish_y)) <= 1000:
      print("happy")
      return
    for i in range(n):
      if not visited[i]:
        nx, ny = data[i]
        # 갈 수 있는 길로 이동해본다.
        if (abs(x - nx) + abs(y - ny)) <= 1000:
          q.append((nx, ny))
          visited[i] = True
  # 도착 지점으로 갈 수 없는 경우
  print("sad")
  return 

for _ in range(int(input())):
  n = int(input())
  data = []
  # 집, 편의점, 도착지점 정보 입력
  home_x, home_y = map(int, input().split())
  for _ in range(n):
    x, y = map(int,input().split())
    data.append((x, y))
  finish_x, finish_y = map(int,input().split())
  # 실행
  bfs(home_x, home_y)