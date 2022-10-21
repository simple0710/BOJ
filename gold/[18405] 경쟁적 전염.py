from collections import deque
import sys
input = sys.stdin.readline

def move():
   dx = [-1, 1, 0, 0]
   dy = [0, 0, -1, 1]

   q = deque()
   # 바이러스의 정보를 담는다.
   for i in range(1, k+1):
      for j in range(n):
         for w in range(n):
            if graph[j][w] == i:
               q.append((i, j, w))
   ''' # 바이러스 입력 및 바로 정보를 얻을 수 있다.
   graph = [[] for _ in range(n)]
   for i in range(n):
      graph.append(list(map(int,input().split())))
      for j in range(n):
         if graph[i][j] != 0:
            q.append((graph[i][j], i, j))
   '''
   time = 0
   while q:
      # 시간이 된 경우 종료
      if time == s:
         break
      # 한 사이클을 실행한다.
      for _ in range(len(q)):
         # 바이러스 번호, 세로, 가로 위치
         v, x, y = q.popleft()
         for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
               graph[nx][ny] = v
               q.append((v, nx, ny))
      # 시간 증가
      time += 1
   # 정답 반환
   return graph[a-1][b-1]

n, k = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
s, a, b = map(int,input().split())

print(move())