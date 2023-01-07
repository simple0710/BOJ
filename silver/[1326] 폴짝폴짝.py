# 2022/12/17 BFS
# https://www.acmicpc.net/problem/1326
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
  visited = [False] * N
  visited[s-1] = 1
  q = deque()
  q.append(s-1)
  while q:
    v = q.popleft()
    if v == e-1:
      return visited[v] - 1
    # 앞, 뒤로 갈 수 있는 범위를 확인한다.
    for i in range(v, N, arr[v]):
      if not visited[i]:
        visited[i] = visited[v] + 1
        q.append(i)
    for i in range(v, -1, -arr[v]):
      if not visited[i]:
        visited[i] = visited[v] + 1
        q.append(i)
  return -1

N = int(input())
arr = list(map(int,input().split()))
s, e = map(int,input().split())

# 정답 출력
print(bfs())
