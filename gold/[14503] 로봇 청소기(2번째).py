import sys
input = sys.stdin.readline

n, m = map(int,input().split())
r, c, d = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0] # 0, 2 = 북 남
dy = [0, 1, 0, -1] # 1, 3 = 동 서

graph[r][c] = 2
cnt = 1
flag = 0
# 더 이상 갈 곳이 없으면 종료
while flag != 1:
   # 왼쪽부터 확인한다.
   for i in range(4):
      # 왼쪽을 먼저 확인한다.
      d -= 1
      if d < 0:
         d = 3
      # 다음 이동거리 계산
      nx = r + dx[d]
      ny = c + dy[d]
      # 범위를 벗어나지 않고 청소하지 않은 구역인 경우 청소 실시 및 이동
      # 그 후 처음부터 실시한다.
      if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
         cnt += 1
         graph[nx][ny] = 2
         r = nx
         c = ny
         break
      # 원래 보던 방향을 볼 경우 뒤를 확인한다.
      if i == 3:
         r = r - dx[d]
         c = c - dy[d]
         # 만약 벽이면 flag = 1, 종료
         if graph[r][c] == 1:
            flag = 1
            break
# 결과 출력
print(cnt)