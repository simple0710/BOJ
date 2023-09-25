# 2023/09/24 DataStructures, Disjoint-Set
# https://www.acmicpc.net/problem/1976
import sys
input = sys.stdin.readline

def find(x): # 부모 찾기
  if parent[x] != x:
    parent[x] = find(parent[x])
  return parent[x]

def union(a, b): # 부모 합치기
  a = find(a)
  b = find(b)
  parent[max(a, b)] = min(a, b)

def solution(N, M, connection_data, travel_data):
  global parent
  parent = [i for i in range(N)]
  for i in range(N):
    for j in range(N):
      # 연결된 도시간 부모 합치기
      if connection_data[i][j] and find(i) != find(j):
        union(i, j)

  check = parent[travel_data[0]-1]
  for i in travel_data:
    if parent[i-1] != check: # 부모가 다른 여행지가 있는 경우
      return 'NO'
  return 'YES' # 모든 도시가 연결되어 있는 경우

def main():
  N = int(input())
  M = int(input())
  connection_data = [list(map(int,input().split())) for _ in range(N)]
  travel_data = list(map(int,input().split()))
  print(solution(N, M, connection_data, travel_data)) # 코드 실행 및 정답 출력

if __name__ == "__main__":
  main()