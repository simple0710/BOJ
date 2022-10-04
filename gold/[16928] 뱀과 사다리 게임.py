from collections import deque
# 너비 우선 탐색
def bfs():
  q = deque([1])
  visited[1] = True
  while q:
    start = q.popleft()
    for step in range(1, 7):
      n_start = lad_sna[start + step]
      # 제한 구역 내에서 방문하지 않은 구역인 경우
      if 0 < n_start <= 100 and not visited[n_start]:
        q.append(n_start)
        visited[n_start] = True
        board_cnt[n_start] = board_cnt[start] + 1
        # 도착할 경우 board_cnt 반환
        if visited[100] == True:
          return board_cnt[100]

n, m = map(int,input().split())

# 사다리와 뱀의 정보를 한 곳에 담는다.
lad_sna = dict()
for i in range(1,101):
  lad_sna[i] = i
for _ in range(n+m):
  a, b = map(int,input().split())
  lad_sna[a] = b

visited = [False] * 101
board_cnt = [0] * 101

print(bfs())

