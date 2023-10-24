# 2023/09/08 BFS
# https://www.acmicpc.net/problem/2251
from collections import deque
import sys
input = sys.stdin.readline

def visited_check(x, y): # 방문 기록 확인
  if not visited[x][y]:
    visited[x][y] = True
    q.append((x, y))

def solution(a, b, c):
  global q, visited
  q = deque([(0, 0)])
  visited = [[False] * (b+1) for _ in range(a+1)]
  visited[0][0] = True
  res = []
  while q:
    x, y = q.popleft()
    z = c - x - y
    if x == 0:
      res.append(z)
    # x -> y
    xy = min(x, b-y)
    visited_check(x-xy, y+xy)

    # x -> z
    xz = min(x, c-z)
    visited_check(x-xz, y)

    # y -> x
    yx = min(y, a-x)
    visited_check(x+yx, y-yx)

    # y -> z
    yz = min(y, c-z)
    visited_check(x, y-yz)

    # z -> x
    zx = min(z, a-x)
    visited_check(x+zx, y)

    # z -> y
    zy = min(z, b-y)
    visited_check(x, y+zy)

  return res # 정답 반환

def main():
  A, B, C = map(int,input().split())
  res = sorted(solution(A, B, C))
  for i in res: # 정답 출력
    print(i, end=' ')

if __name__ == "__main__":
  main()