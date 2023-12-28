# 2023/12/28 BFS, DFS
# https://www.acmicpc.net/problem/14248
from collections import deque

def solution():
  q = deque([s])
  visited = [False] * N
  visited[s] = True
  res = 1
  while q:
    now = q.popleft()
    # 왼쪽, 오른쪽 이동
    for i in [road[now], -road[now]]:
      next = now + i
      if 0 <= next < N and not visited[next]:
        visited[next] = True
        q.append(next)
        res += 1
  # 방문 가능한 위치 반환
  return res

def main():
  global N, road, s
  N = int(input())
  road = list(map(int,input().split()))
  s = int(input()) - 1
  # 방문 가능한 위치 출력
  print(solution())

if __name__ == "__main__":
  main()