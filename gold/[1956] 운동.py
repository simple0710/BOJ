# 2023/12/14 Floyd-Warshall
# https://www.acmicpc.net/problem/1956
import sys
input = sys.stdin.readline
INF = sys.maxsize

def solution():
  res = INF
  # 시작 지점
  for i in range(1, V+1):
    # 도착 지점
    for j in range(1, V+1):
      # 거쳐가는 지점
      for k in range(1, V+1):
        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        if i == j and dist[i][j] != INF: res = min(res, dist[i][j])
  # 최소 사이클의 도로 길이의 합이 존재한다면 길이 반환
  return res if res != INF else -1

def main():
  global V, E, dist
  V, E = map(int,input().split())
  dist = [[INF] * (V + 1) for _ in range(V+1)]
  for _ in range(E):
    a, b, c = map(int,input().split())
    dist[a][b] = c
  print(solution()) # 최소 사이클의 도로 길이의 합 출력

if __name__ == "__main__":
  main()