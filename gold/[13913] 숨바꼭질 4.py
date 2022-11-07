# 2022/11/07 너비우선탐색
from collections import deque
import sys
input = sys.stdin.readline
MAX = 100001

# 이동 경로를 출력한다.
def path(x):
  arr = []
  temp = x
  for _ in range(data[x] + 1):
    arr.append(temp)
    temp = move[temp]
  print(' '.join(map(str, arr[::-1])))

# 너비우선탐색
def bfs():
  q = deque()
  q.append(N)
  while q:
    now = q.popleft()
    # 동생을 찾은 경우 결과 출력 후 종료
    if now == K:
      print(data[now]) # 횟수 출력
      path(now) # 이동 경로 출력
      return
    # 이동
    for next in [now + 1, now-1, now*2]:
      if 0 <= next < MAX and data[next] == 0:
        data[next] = data[now] + 1
        q.append(next)
        # 어디로부터 왔는지를 저장한다.
        move[next] = now

# 정보 입력
N, K = map(int,input().split())
data = [0] * MAX
move = [0] * MAX

# 탐색 시작 및 출력
bfs()
