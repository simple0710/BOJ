# 2022/12/03 BFS
# https://www.acmicpc.net/problem/2234
from collections import deque
import sys
input = sys.stdin.readline

# 팀과 방의 크기 확인
def team_check(team, x, y):
  check_place[x][y] = team
  q = deque()
  cnt = 1
  q.append((x, y))
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < M and 0 <= ny < N and not check_place[nx][ny]:
        # 만약 벽이 있다면 meet 리스트에 추가한다.
        if castle[x][y][-i-1] == '1':
          meet[team-1].append((nx, ny))
          continue
        # 팀 지정
        else:  
          q.append((nx, ny))
          check_place[nx][ny] = team
          cnt += 1
  # 총 칸 수를 반환한다.
  return cnt

if __name__ == "__main__":
  N, M = map(int,input().split())
  castle = []
  for i in range(M):
    castle.append(list(map(int,input().split())))
    for j in range(N):
      # 4자리 이진수로 변경
      castle[i][j] = format(castle[i][j], 'b')
      if len(castle[i][j]) < 4:
        castle[i][j] = '0' * (4 - len(castle[i][j])) + castle[i][j]

  dx = [0, -1, 0, 1]
  dy = [-1, 0, 1, 0]
  check_place = [[False] * N for _ in range(M)]
  cnt_dict = {}
  meet = []
  team = 1
  # 팀의 수와 방의 개수를 구한다.
  for i in range(M):
    for j in range(N):
      if not check_place[i][j]:
        meet.append([])
        cnt_dict[team] = team_check(team, i, j)
        team += 1

  res = 0
  # 벽 부서서 얻는 방의 크기를 구한다.
  for i in range(len(meet)):
    check = cnt_dict[i + 1] # 해당 방의 넓이
    for x, y in meet[i]:
      if i + 1 != check_place[x][y]:
        res = max(res, check + cnt_dict[check_place[x][y]])

  # 정답 출력
  print(team-1) # 이 성에 있는 방의 개수
  print(max(cnt_dict.values())) # 가장 넓은 방의 넓이
  print(res) # 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기