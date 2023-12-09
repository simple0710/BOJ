# 2023/12/09 Dijkstra, DP
# https://www.acmicpc.net/problem/11909
import sys, heapq
input = sys.stdin.readline
MAX = int(1e9)

# 1. Dijkstra
def solution(N, graph):
  q = [(0, (0, 0))]
  cost_graph = [[MAX] * N for _ in range(N)]
  cost_graph[0][0] = 0
  while q:
    cost, now = heapq.heappop(q)
    x, y = now
    if cost_graph[x][y] < cost: continue
    for nx, ny in [(x+1, y), (x, y+1)]:
      if 0 <= nx < N and 0 <= ny < N:
        total_cost = cost 
        if graph[x][y] <= graph[nx][ny]: total_cost += graph[nx][ny] - graph[x][y] + 1
        # 해당 위치보다 비용이 작다면 다음을 수행
        if cost_graph[nx][ny] > total_cost:
          cost_graph[nx][ny] = total_cost
          heapq.heappush(q, (total_cost, (nx, ny)))
  return cost_graph[N-1][N-1] # 버튼을 누르는데 들인 비용 반환

# 2. DP
def solution2(N, graph):
  for i in range(N): graph[i] = [0] + graph[i]
  graph = [[0] * (N+1)] + graph
  dp = [[0] * (N+1) for _ in range(N+1)]
  for x in range(1, N+1):
    for y in range(1, N+1):
      if (x, y) == (1, 1): continue
      check = MAX
      # 현재 위치에서 위, 왼쪽을 확인
      for nx, ny in [(x-1, y), (x, y-1)]:
        v = dp[nx][ny]
        if 0 < nx and 0 < ny: # 범위 내인 경우만 확인
          if graph[x][y] >= graph[nx][ny]: # 현재 위치가 비교할 위치보다 수가 큰 경우
            # 이동하기 위한 비용 계산
            v += (graph[x][y] - graph[nx][ny] + 1)
          # 비용 갱신
          check = min(check, v)
      dp[x][y] = check
  return dp[N][N] # 버튼을 누르는데 들인 비용 반환

def main():
  N = int(input())
  graph = [list(map(int,input().split())) for _ in range(N)]
  print(solution2(N, graph)) # 버튼을 누르는데 들인 비용 출력

if __name__ == "__main__":
  main()