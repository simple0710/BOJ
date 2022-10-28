# 2022/10/24 너비우선탐색
from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
  q = deque()
  q.append(v)
  visited[v] = True
  while q:
    v = q.popleft()
    # 목적지에 도착했을 경우 횟수 반환
    if v == G:
      return cnt[G]
    for move in moves:
      nv = v + move
      # 방문한 적이 없고 범위 내인 경우
      if 1 <= nv <= F and not visited[nv]:
        visited[nv] = True
        cnt[nv] = cnt[v] + 1
        q.append(nv)
  return "use the stairs"

# 정보 입력
F, S, G, U, D = map(int,input().split())
visited = [False] * (F + 1)
cnt = [0] * (F + 1)
moves = [U, -D]

# 탐색 시작 및 결과 출력
print(bfs(S))