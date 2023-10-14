# 2023/10/14 PriorityQueue, DataStructures
# https://www.acmicpc.net/problem/2075
import sys, heapq
input = sys.stdin.readline

def main():
  N = int(input())
  q = []
  # N * N표 입력
  for _ in range(N):
    row = list(map(int,input().split()))
    for j in row:
      # 길이가 N미만인 경우 j추가
      # 길이가 N이상인 경우 q의 가장 작은 값과 j중 큰 값을 추가
      heapq.heappush(q, j if len(q) < N else max(heapq.heappop(q), j))
  print(heapq.heappop(q)) # 정답 출력

if __name__ == "__main__":
  main()