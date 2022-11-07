# 2022/11/03 너비우선탐색
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
  dr = [0, 0, 1, -1] 
  dc = [1, -1, 0, 0]
  change_dir = ((2, 3), (2, 3), (0, 1), (0, 1))
  visited = [[[0] * 4 for _ in range(N)] for _ in range(M)]
  visited[sm-1][sn-1][sw-1] = 1
  q = deque()
  q.append((sm-1, sn-1, sw-1, 0))
  while q:
    r, c, d, cnt = q.popleft()
    # 목표 위치와 방향에 도착하면 cnt 리턴
    if (r, c, d) == (fm-1, fn-1, fw-1):
      return cnt
    
    # 1, 2, 3 칸 직진
    for dis in range(1, 4):
      nr = r + dr[d] * dis
      nc = c + dc[d] * dis
      nd = d
      # 맵을 벗어나거나 벽을 만날 경우 종료
      if not (0 <= nr < M and 0 <= nc < N) or data[nr][nc]:
        break
      if visited[nr][nc][nd]:
        continue
      q.append((nr, nc, nd, cnt + 1))
      visited[nr][nc][nd] = 1
    # 방향 바꾸기
    for nd in change_dir[d]:
      if visited[r][c][nd]:
        continue
      q.append((r, c, nd, cnt+1))
      visited[r][c][nd] = 1

if __name__ == "__main__":
  M, N = map(int,input().split())
  data = [list(map(int,input().split())) for _ in range(M)]
  sm, sn, sw = map(int,input().split())
  fm, fn, fw = map(int,input().split())

  print(bfs())