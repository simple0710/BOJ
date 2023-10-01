# 2023/10/01 BFS
# https://www.acmicpc.net/problem/12869
from collections import deque
import sys
input = sys.stdin.readline

def solution(SCV):
  SCV = SCV + [0] * (3-len(SCV))
  q = deque([(SCV, 0)])
  visited = set()
  visited.add(tuple(SCV))
  while q:
    v, cnt = q.popleft()
    if max(v) <= 0: # 모든 SCV를 잡은 경우
      return cnt
    for i in range(3):
      a = v[i]
      if a > 0: # 남아있는 SCV가 있는 경우
        na = a - 9 if a - 9 > 0 else 0
        for b, c in [(v[(i+1)%3], v[(i+2)%3]), (v[(i+2)%3], v[(i+1)%3])]:
          nb = b - 3 if b - 3 > 0 else 0
          nc = c - 1 if c - 1 > 0 else 0
          if (na, nb, nc) not in visited: # 방문 기록에 없는 경우
            q.append(((na, nb, nc), cnt+1))
            visited.add((na, nb, nc))

def main():
  N = int(input())
  SCV = list(map(int,input().split()))
  print(solution(SCV)) # 횟수의 최솟값 출력

if __name__ == "__main__":
  main()