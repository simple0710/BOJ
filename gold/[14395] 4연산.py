# 2022/11/29 너비 우선 탐색
# https://www.acmicpc.net/problem/14395ㅇ
from collections import deque
import sys
input = sys.stdin.readline

# 너비 우선 탐색
def bfs():
  q = deque()
  q.append((s, ''))
  while q:
    v, r = q.popleft()
    # 정답인 경우 r 반환
    if v == t:
      return r
    if v == 0:
      continue
    for idx, value in enumerate([(v*v), (v+v), (v-v), int(v/v)]):
      # 해당 값 안에 있고 value가 check에 없는 경우
      if 0 <= value <= t and value not in check:
        if idx == 0:
          nr = r + '*'
        elif idx == 1:
          nr = r + '+'
        elif idx == 2:
          nr = r + '-'
        else:
          nr = r + '/'
        q.append((value, nr))
        check.add(value)
  # 도달할 수 없는 경우 -1 반환
  return -1

# 정보 입력
s, t = map(int,input().split())
# 처음부터 값이 같다면 0 출력
if s == t:
  print(0)
# 아닌 경우 탐색 시작
else:
  check = set([s])
  # 정답 출력
  print(bfs())