# 2023/03/08 bfs
# https://www.acmicpc.net/problem/16953
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
  q = deque()
  q.append((B, 1))
  while q:
    v, cnt = q.popleft()
    if v == A: # A를 만든 경우 cnt 반환
      return cnt
    if v > 1:
      values = []
      if not v % 2: # 짝수인 경우 2로 나눈 값을 추가
        values.append((v // 2))
      if str(v)[-1] == '1': # 끝이 1인 경우 마지막을 뺀 값을 추가
        values.append(int(str(v)[:-1]))
      for value in values:
        q.append((value, cnt+1))
  return -1 # A를 만들지 못한 경우 -1 반환 

A, B = map(int,input().split())

# 탐색 시작
res = bfs()

# 정답 출력
print(res)