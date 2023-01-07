# 2022/12/13 BFS
# https://www.acmicpc.net/problem/13460
from collections import deque
import sys
input = sys.stdin.readline

def bfs(rx, ry, bx, by):
  # 방문 기록을 4개로 나누어 저장한다.
  visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
  visited[rx][ry][bx][by] = True
  q = deque()
  q.append((rx, ry, bx, by, 1))
  while q:
    rx, ry, bx, by, depth = q.popleft()
    if depth > 10: # 10번 이상인 경우는 종료
      break
    for i in range(4):
      n_rx, n_ry, r_cnt = move(rx, ry, dx[i], dy[i])
      n_bx, n_by, b_cnt = move(bx, by, dx[i], dy[i])
      # 파란 구슬이 빠진 경우는 continue
      if board[n_bx][n_by] == 'O':
        continue
      # 빨간 구슬만 빠진 경우 depth(횟수)를 리턴한다.
      if board[n_rx][n_ry] == 'O':
        return depth
      # 같은 위치에 존재하는 경우
      if n_rx == n_bx and n_ry == n_by:
        # 이동 거리를 비교한 후 이동 거리가 더 큰 구슬은
        # 이동한 방향의 한칸 전에 배치한다.
        if r_cnt > b_cnt:
          n_rx -= dx[i]
          n_ry -= dy[i]
        else:
          n_bx -= dx[i]
          n_by -= dy[i]
      # 방문하지 않은 경우 True로 하고 q에 추가한다.
      if not visited[n_rx][n_ry][n_bx][n_by]:
        visited[n_rx][n_ry][n_bx][n_by] = True
        q.append((n_rx, n_ry, n_bx, n_by, depth+1))
  # 10번 이하로 빼낼 수 없는 경우 -1 반환
  return -1
# 벽이나 구멍에 빠지는 경우까지 더한다.
def move(x, y, dx, dy):
  cnt = 0 # 이동 거리
  while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
    x += dx
    y += dy
    cnt += 1
  # 이동한 위치, 거리를 반환한다.
  return x, y, cnt

if __name__ == "__main__":
  N, M = map(int,input().split())
  board = []
  for i in range(N):
    board.append(list(map(str, input().rstrip())))
    for j in range(M):
      if board[i][j] == 'R':
        board[i][j] = '.'
        rx, ry = i, j
      elif board[i][j] == 'B':
        board[i][j] = '.'
        bx, by = i, j

  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  # BFS 후 정답 출력
  print(bfs(rx, ry, bx, by))