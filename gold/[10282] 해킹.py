# 2023/12/05 Dijkstra
# https://www.acmicpc.net/problem/10282
import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

def solution(n, computer_tree, start):
  q = []
  heapq.heappush(q, (start, 0))
  visited = [INF] * (n + 1)
  visited[start] = 0
  while q:
    now, now_cost = heapq.heappop(q)
    if visited[now] < now_cost: # 현재 시간이 더 작다면 넘긴다.
      continue
    for next, cost in computer_tree[now]:
      next_cost = now_cost + cost # 다음 컴퓨터를 감염시키는 시간
      if next_cost < visited[next]: # 더 짧은 시간인 경우 시간 갱신
        visited[next] = next_cost
        heapq.heappush(q, (next, next_cost))
  result = [i for i in visited if i != INF]
  return (len(result), max(result)) # 감염되는 컴퓨터 수, 걸리는 시간 반환

def main():
  T = int(input())
  for _ in range(T):
    n, d, c = map(int,input().split())
    computer_tree = [[] for _ in range(n+1)]
    for _ in range(d):
      a, b, s = map(int,input().split())
      computer_tree[b].append((a, s))
    # 감염되는 컴퓨터 수, 걸리는 시간 출력
    print(*solution(n, computer_tree, c))

if __name__ == "__main__":
  main()