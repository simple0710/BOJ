# 2023/08/30 Recursion
# https://www.acmicpc.net/problem/2448
import sys
input = sys.stdin.readline

def get_star(x, y, N):
  if N == 3:
    graph[x][y] = '*'
    graph[x+1][y-1] = graph[x+1][y+1] = '*'
    for i in range(-2, 3):
      graph[x + 2][y + i] = '*'
  else:
    next_n = N // 2
    get_star(x, y, next_n) # 중간
    get_star(x + next_n, y - next_n, next_n) # 왼쪽
    get_star(x + next_n, y + next_n, next_n) # 오른쪽

def solution():
  global graph
  graph = [[' '] * 2 * N for _ in range(N)]
  # 별 채우기 시작
  get_star(0, N - 1, N)
  # 별 모양을 출력
  for i in graph: print(''.join(i))

if __name__ == "__main__":
  N = int(input())
  solution()