# 2023/12/02 DataStructures, Greedy, PriorityQueue
# https://www.acmicpc.net/problem/13975
import heapq

def solution(data):
  heapq.heapify(data)
  res = 0
  # 하나의 소설이 될 때까지 가장 작은 비용의 두 파일을 계속 합친다.
  while len(data) > 1:
    v = heapq.heappop(data) + heapq.heappop(data)
    res += v
    heapq.heappush(data, v)
  return res # 비용의 총 합 반환

def main():
  T = int(input())
  for _ in range(T):
    K = int(input())
    data = list(map(int,input().split()))
    print(solution(data)) # 비용의 총 합 출력

if __name__ == "__main__":
  main()