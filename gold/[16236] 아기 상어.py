# 2022/11/14 BFS, Simulation
from collections import deque
import sys
input = sys.stdin.readline

# 먹이 위치에 대한 정의
def bfs(start_x, start_y):
  visited = [[False] * N for _ in range(N)]
  visited[start_x][start_y] = True
  q = deque()
  q.append((start_x, start_y, 0))
  min_dist = int(1e9)
  dist_list = []
  while q and fish_cnt:
    x, y, dist = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
        # 해당 칸이 상어의 현재 크기보다 작다면 일단 움직인다.
        if data[nx][ny] <= shark_size:
          visited[nx][ny] = True
          # 자신보다 작다면 최소 거리 저장 및 dist_list에 해당 먹이에 대한 기록 저장
          if 0 < data[nx][ny] < shark_size:
            min_dist = dist
            dist_list.append((dist+1, nx, ny))
          # 최소 길이만큼만 움직인다.
          if dist+1 <= min_dist:
            q.append((nx, ny, dist+1))
  # 먹을 수 있는 먹이가 있는 경우 dist_list[0]을 반환(가장 빨리 먹을 수 있는 먹이)
  if dist_list:
    dist_list.sort()
    return dist_list[0]
  else:
    return False

if __name__ == "__main__":
  # 정보 입력
  N = int(input())
  data = []
  fish_cnt = 0

  shark_size = 2
  dx = [-1, 0, 0, 1]
  dy = [0, -1, 1, 0]
  time = 0
  eat_cnt = 0
  # 상어의 위치 및 먹이에 대한 위치 기록
  for i in range(N):
    data.append(list(map(int,input().split())))
    for j in range(N):
      if data[i][j] != 0 and data[i][j] != 9:
        fish_cnt += 1
      elif data[i][j] == 9:
        start_x, start_y = i, j
        data[i][j] = 0

  while fish_cnt:
    # 시작 위치에서 탐색을 시작한다.
    result = bfs(start_x, start_y)
    # 결과가 나오지 않았을 경우 종료
    if not result:
      break
    # 기록된 x, y, time을 저장
    start_x, start_y = result[1], result[2]
    time += result[0]
    # 먹은 횟수와 먹은 고기 수 조정
    eat_cnt += 1
    fish_cnt -= 1
    # 먹은 고기의 수와 상어의 크기가 같다면 size += 1, 먹은 횟수 초기화
    if shark_size == eat_cnt:
      shark_size += 1
      eat_cnt = 0
    # 0 처리
    data[start_x][start_y] = 0
  # 정답 출력
  print(time)