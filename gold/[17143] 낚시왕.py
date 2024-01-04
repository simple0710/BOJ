# 2024/01/04 Implementation, Simulation
# https://www.acmicpc.net/problem/17143
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

# 상어를 움직인다.
def shark_move(r, c, s, d):
  while s: # 시간만큼 확인
    nr = r + dr[d]
    nc = c + dc[d]
    # 범위 내인 경우 이동한 것으로 간주한다.
    if 0 <= nr < R and 0 <= nc < C:
      r, c = nr, nc
      s -= 1
    else: # 범위 밖으로 나갈려고 하는 경우 방향을 전환한다.
      if (d % 2 == 0): d += 1
      else: d -= 1
  return (r, c, d) # 이동할 위치 반환

# 새로운 배열에 상어의 이동을 저장한 뒤 반환한다.
def get_new_board(board):
  new_board = [[[] for _ in range(C)] for _ in range(R)]
  # 상어가 이동할 위치에 값을 추가한다.
  for i in range(R):
    for j in range(C):
      if board[i][j]:
        s, d, z = board[i][j].pop()
        nr, nc, nd = shark_move(i, j, s, d)
        new_board[nr][nc].append((s, nd, z))
  # 사이즈가 가장 큰 상어만 남긴다.
  for i in range(R):
    for j in range(C):
      if new_board[i][j]:
        max_size_set = sorted(new_board[i][j], key=lambda x : -x[2])[0]
        new_board[i][j].clear()
        new_board[i][j].append(max_size_set)
  return new_board # 이동을 마친 배열 반환

def solution(board):
  res = 0
  # 현재 위치
  for now in range(C):
    # 상어를 낚는다.
    for i in range(R):
      if board[i][now]: # 상어가 있으면 잡은 뒤에 종료한다.
        res += board[i][now].pop()[2]
        break
    board = get_new_board(board) # 상어가 이동한다.
  return res # 낚시왕이 잡은 상어 크기의 합을 반환한다.

def main():
  global R, C, M, board
  R, C, M = map(int,input().split())
  board = [[[] for _ in range(C)] for _ in range(R)]
  for _ in range(M):
    r, c, s, d, z = map(int,input().split())
    board[r-1][c-1].append((s, d-1, z))
  print(solution(board)) # 낚시왕이 잡은 상어 크기의 합을 출력한다.

if __name__ == "__main__":
  main()