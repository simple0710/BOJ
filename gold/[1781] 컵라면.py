# 2023/12/04 DataStructures, Greedy, PriorityQueue
# https://www.acmicpc.net/problem/1781
import heapq, sys
input = sys.stdin.readline

def solution(N, homeworks):
  homeworks.sort() # 시간 및 컵라면 개수 오름차 정렬
  q = []
  for time, value in homeworks:
    heapq.heappush(q, value)
    # 풀 수 있는 문제 중 컵라면을 가장 많이 받을 수 있는 문제를 해결한다.
    if time < len(q):
      heapq.heappop(q)
  return sum(q) # 최대 컵라면 수 반환

def main():
  N = int(input())
  homeworks = [list(map(int,input().split())) for _ in range(N)]
  print(solution(N, homeworks)) # 최대 컵라면 수 출력

if __name__ == "__main__":
  main()