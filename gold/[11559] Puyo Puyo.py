# 2022/11/12 너비우선탐색
from collections import deque

def bfs():
  res = 0
  b = []
  while True:
    cnt = 0
    # 전 지역을 탐색한다.
    for x in range(6):
      for y in range(12):
        # 해당 공간이 색을 가지고 있고 주변 영역의 합이 4 이상인 경우
        if data[x][y] != '.' and data[x][y] != 1 and check(x, y):
          q = deque()
          q.append((x, y))
          col = data[x][y]
          cnt = 1
          while q:
            x, y = q.popleft()
            for i in range(4):
              nx = x + dx[i]
              ny = y + dy[i]
              if 0 <= nx < 6 and 0 <= ny < 12 and col == data[nx][ny]:
                data[nx][ny] = 1
                b.append((nx, ny))
                q.append((nx, ny))
    # 1로 체크한 공간을 삭제 후 공간을 민다.
    while b:
      x, y = b.pop(0)
      del data[x][data[x].index(1)]
      data[x].insert(0, '.')
    # 만약 cnt == 1인 경우 횟수를 증가시킨다.
    if cnt:
      res += cnt
    # 변함이 없는 경우 정답 반환
    else:
      return res

# 주변 공간을 확인한다.
def check(x, y):
  q = deque()
  q.append((x, y))
  visited = [[False] * 12 for _ in range(6)]
  visited[x][y] = True
  cnt = 1
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < 6 and 0 <= ny < 12 and not visited[nx][ny]:
        if data[nx][ny] == data[x][y]:
          cnt += 1
          q.append((nx, ny))
          visited[nx][ny] = True
  # 주변 공간이 4인 경우 True 반환
  if cnt >= 4:
    return True
  else:
    return False

# 정보 입력
game = []
for i in range(12):
  game.append(list(map(str, input())))

data = []
# y축을 x축으로 변환
for i, value in enumerate(zip(*game)):
  data.append(list(value))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 탐색 및 정답 출력
print(bfs())