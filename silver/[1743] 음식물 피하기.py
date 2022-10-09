import sys
sys.setrecursionlimit(10**6)

# 깊이 우선 탐색
def dfs(x, y):
  global cnt
  data[x][y] = 0
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 1:
      cnt += 1
      dfs(nx,ny)

# 값 설정
n, m, k = map(int,input().split())

data = [[0] * m for _ in range(n)]
for _ in range(k):
  a, b = map(int,input().split())
  data[a-1][b-1] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0
for i in range(n):
  for j in range(m):
    # 음식물을 만난 경우
    if data[i][j] == 1:
      cnt = 1 # cnt 초기화
      dfs(i,j)
      answer = max(answer, cnt)

# 출력
print(answer)