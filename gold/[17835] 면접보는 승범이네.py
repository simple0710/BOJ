# 2023/12/07 Dijkstra
# https://www.acmicpc.net/problem/17835
import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

def solution(interview_room):
  distance = [INF] * (N+1)
  q = []
  # 모든 면접장에서 시작
  for start in interview_room:
    heapq.heappush(q, (start, 0))
    distance[start] = 0
  while q:
    now, now_distance = heapq.heappop(q)
    if distance[now] < now_distance:
      continue
    for next, next_distance in graph[now]:
      total_distance = now_distance + next_distance
      if distance[next] > total_distance:
        distance[next] = total_distance
        heapq.heappush(q, (next, total_distance))
  # 결과 확인
  min_number, max_distance = 0, 0
  for idx, dis in enumerate(distance):
    if dis != INF and max_distance < dis:
      min_number, max_distance = idx, dis
  # 가장 먼 도시와 그 거리 반환
  return (min_number, max_distance)

def main():
  global N, M, K, graph
  N, M, K = map(int,input().split())
  graph = [[] for _ in range(N+1)]
  for _ in range(M):
    U, V, C = map(int,input().split())
    graph[V].append((U, C)) # 그래프 진행 방향 변경
  interview_room = [i for i in map(int,input().split())]
  # 가장 먼 도시의 번호와 거리 출력
  print(*solution(interview_room), sep='\n')

if __name__ == "__main__":
  main()