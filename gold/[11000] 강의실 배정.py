# 2023/08/20 DataStructures, Greedy, Sorting, PriorityQueue
# https://www.acmicpc.net/problem/11000
import heapq, sys
input = sys.stdin.readline

def solution(time):
  s, t = time.pop(0)
  check = [t]
  res = 1
  for s, t in time:
    v = heapq.heappop(check)
    if v > s: # 시작 시간보다 더 큰 경우
      heapq.heappush(check, v) # 원래 자리에 추가
    heapq.heappush(check, t) # 끝나는 시간 추가
    res = max(res, len(check))
  return res # 정답 반환

def main():
  N = int(input())
  time = []
  for _ in range(N):
    s, t = map(int,input().split())
    time.append((s, t))
  time.sort()
  print(solution(time)) # 탐색 및 정답 출력

if __name__ == "__main__":
  main()