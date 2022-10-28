from collections import deque
import sys
input = sys.stdin.readline

# 토마토 익기 시작
def solution():
  dx = [-1, 1, 0, 0, 0, 0]
  dy = [0, 0, -1, 1, 0, 0]
  dh = [0, 0, 0, 0, -1, 1]

  while q:
    hei, x, y = q.popleft()
    for i in range(6):
      nx = x + dx[i]
      ny = y + dy[i]
      nh = hei + dh[i]
      # 범위 내에 익지 않은 토마토가 있을 경우 +1 로 익게 함
      if 0 <= nx < n and 0 <= ny < m and 0 <= nh < h and data[nh][nx][ny] == 0:
        data[nh][nx][ny] = data[hei][x][y] + 1
        q.append((nh, nx, ny))

# 토마토가 전부 익었는지 확인
def result():
  answer = 1
  for i in data:
    for j in i:
      if j.count(0) > 0: # 익지 않은 토마토가 있는 경우 -1 반환
        return -1
      answer = max(max(j), answer) # 가장 큰 일 수를 구함
  return answer - 1 # 1부터 시작했기 때문에 -1 을 한다.

m, n, h = map(int,input().split()) # 가로, 세로, 높이
data = [[] for _ in range(h)]
q = deque()
# 토마토 정보 입력 및 토마토 위치 저장해두기
for i in range(h):
  for j in range(n):
    data[i].append(list(map(int,input().split())))
    for k in range(m):
      if data[i][j][k] == 1:
        q.append((i, j, k))
# 익기 시작
# 만약 0이 없어도 1 - 1 = 0 이 출력 된다.
solution()
print(result())