n, m = map(int, input().split())
x, y, d = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
move_data = [list([0] * m) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
move_data[x][y] = 1
cnt = 1
turn_time = 0

while True:
  # 왼쪽으로 회전
  d -= 1
  if d < 0 :
    d = 3
  nx = x + dx[d]
  ny = y + dy[d]
  # 아직 접근하지 않은 구역이 있을 경우
  if data[nx][ny] == 0 and move_data[nx][ny] == 0:
    move_data[nx][ny] = 1
    cnt += 1
    turn_time = 0
    x, y = nx, ny
    continue
  else:
    turn_time += 1 
  # 원 상태로 복귀했을 때
  if turn_time == 4:
    # 이전 자리로 돌아감
    nx = x - dx[d]
    ny = y - dy[d]
    # 접근 할 수 있는 경우
    # move_data[nx][ny] == 0 으로 할 경우 바로 종료 된다.
    # 반복하다 보면 한 쪽 벽에 도달하게 된다.
    if data[nx][ny] == 0:
      x, y = nx, ny
    # 벽에 도달한 경우 종료
    else:
      break
    turn_time = 0

print(cnt)
