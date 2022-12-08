# 2022/12/05 BFS
# https://www.acmicpc.net/problem/12906
from collections import deque

def bfs():
  visited = set()
  q = deque()
  q.append((s[0], s[1], s[2], 0)) # 1, 2, 3 번째 탑의 상태와 cnt
  while q:
    a, b, c, cnt = q.popleft()
    str = a + '/' + b + '/' + c # 구별 지점을 둔다.
    # 해당 칸에 알맞는 원판만 있는 경우 cnt 출력
    if a == 'A' * len(a) and b == 'B' * len(b) and c == 'C' * len(c):
      print(cnt)
      return
    
    if str not in visited:
      visited.add(str)
      # 해당 칸에 옮길만한 원판이 있는 경우
      if len(a) > 0:
        q.append((a[:-1], b+a[-1], c, cnt+1))
        q.append((a[:-1], b, c+a[-1], cnt+1))
      if len(b) > 0:
        q.append((a+b[-1], b[:-1], c, cnt+1))
        q.append((a, b[:-1], c+b[-1], cnt+1))
      if len(c) > 0:
        q.append((a+c[-1], b, c[:-1], cnt+1))
        q.append((a, b+c[-1], c[:-1], cnt+1))

if __name__ == "__main__":
  s = []
  for _ in range(3):
    a = input().split()
    if len(a) > 1:
      s.append(a[-1])
    else:
      s.append('')
  bfs()