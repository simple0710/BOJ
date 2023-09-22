# 2023/09/22 Implementation, Simulation
# https://www.acmicpc.net/problem/17837
import sys
input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 범위 내, 파란 칸인 경우, move_pin을 반환하는 함수
def move_pin_get(now, x, y, nx, ny):
  move_pin = []
  # 범위 안이고, 파란색 칸이 아닌 경우
  if 0 <= nx < N and 0 <= ny < N and board[nx][ny] != 2:
    # 현재 위치의 말까지 이동
    # 데이터는 역 순으로 저장
    while pin_board[x][y]:
      v = pin_board[x][y].pop()
      move_pin.append(v)
      if v == now:
        break
    
    for i in move_pin: # 위치 수정
      pin[i] = [nx, ny, pin[i][2]]

    # 하얀 칸인 경우 위에서 역 순으로 데이터를 저장하였으므로, 역 순으로 정렬
    if board[nx][ny] == 0:
      move_pin = move_pin[::-1]

  return move_pin # 움직인 말 데이터 반환

def solution():
  cnt = 0
  # extend한 후에 이동한 위치로 좌표 수정
  while cnt <= 1000:
    cnt += 1
    for now in range(K): # 모든 말 이동
      x, y, d = pin[now]
      nx = x + dx[d]
      ny = y + dy[d]
      # 말 이동 데이터 저장
      move_pin = move_pin_get(now, x, y, nx, ny)
      if not move_pin: # 벽이거나, 파란 칸인 경우
        # 반대 방향 이동
        if (d + 1) % 2 == 0:
          d -= 1
        else:
          d += 1
        nx = x + dx[d]
        ny = y + dy[d]
        # 말 이동 데이터 저장
        move_pin = move_pin_get(now, x, y, nx, ny)
        if not move_pin: # 벽이거나, 파란 칸인 경우
          nx = x
          ny = y
        pin[now] = [nx, ny, d] # 변환된 현재 말 위치 데이터 저장
      pin_board[nx][ny].extend(move_pin) # 이동한 칸에 이동한 말들 저장
      if len(pin_board[nx][ny]) >= 4: # 4개 이상 겹친 경우 cnt 반환 후 종료
        return cnt
  else: # cnt가 1000을 넘긴 경우
    cnt = -1
  return cnt # cnt 반환

def main():
  global N, K, board, pin, pin_board
  N, K = map(int,input().split())
  board = [list(map(int,input().split())) for _ in range(N)]
  pin_board = [[[] for _ in range(N)] for _ in range(N)]
  pin = []
  for num in range(K):
    x, y, d = map(int,input().split())
    pin.append([x-1, y-1, d-1])
    pin_board[x-1][y-1].append(num)
  print(solution()) # 코드 실행 및 정답 출력

if __name__ == "__main__":
  main()