# 2023/08/25 DFS, Trees
# https://www.acmicpc.net/problem/1167
# 트리의 지름 구하는 방법
# 1. 임의의 점(A)에서 가장 먼 지점(B)을 찾는다
# 2. B에서 가장 먼 지점(C)을 찾는다.
# 3. B-C의 거리가 트리의 지름이다.
import sys
input = sys.stdin.readline

def dfs(now, c):
  for next, nc in graph[now]:
    nc = c + nc
    if distance[next] == -1: # 방분하지 않은 지점에 거리 저장
      distance[next] = nc
      dfs(next, nc)

def solution():
  global distance
  distance = [-1] * (V + 1)
  distance[1] = 0
  dfs(1, 0) # 1부터 시작

  node = distance.index(max(distance))
  distance = [-1] * (V + 1)
  distance[node] = 0
  dfs(node, 0) # 가장 먼 지점부터 시작

  return max(distance) # 정답 반환

if __name__ == "__main__":
  V = int(input())
  graph = [[] for _ in range(V + 1)]
  for _ in range(1, V + 1):
    info = list(map(int,input().split()))[:-1]
    for j in range(1, len(info), 2):
      graph[info[0]].append((info[j], info[j+1]))
  print(solution()) # 탐색 및 정답 출력