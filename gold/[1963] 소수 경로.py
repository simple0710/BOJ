# 2022/12/08 BFS, 에라토스테네스의 체
# https://www.acmicpc.net/problem/1963
from collections import deque
import sys
input = sys.stdin.readline

def prime():
  s = [True] * 10000
  m = int(10000 ** 0.5)
  for i in range(2, m + 1):
    if s[i] == True:
      for j in range(i + i, 10000, i):
        s[j] = False
  # 1000부터 9999의 소수를 구한다.
  return [str(i) for i in range(1000, 10000) if s[i] == True]

def bfs(v):
  q = deque()
  q.append((v, 0))
  visited = set()
  visited.add(v)
  while q:
    v, cnt = q.popleft()
    # M과 같은 경우 횟수 반환
    if v == M:
      return cnt
    # 각 자리에 1에서 9까지 수를 넣어본다.
    for i in range(4):
      nv = list(v)
      for j in range(10):
        nv[i] = j
        tmp = ''.join(map(str,nv))
        # 소수 여부와 방문 기록을 확인한다.
        if tmp in p and tmp not in visited:
          visited.add(tmp)
          q.append((tmp, cnt + 1))

p = prime()
for _ in range(int(input())):
  N, M = map(str,input().split())
  # 탐색
  print(bfs(str(N)))
  
