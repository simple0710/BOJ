# 2023/09/13 DataStructures, Greedy, PriorityQueue
# https://www.acmicpc.net/problem/1715
import sys, heapq
input = sys.stdin.readline

def solution(N, card):
  res = 0
  check = heapq.heappop(card)
  while card:
    v = heapq.heappop(card)
    if check <= v: # 현재 비용이 다음 카드의 비용보다 작거나 같은 경우
      # 카드 묶음을 비교한다.
      res += v + check
      check += v
    else: # 현재 비용이 다음 카드의 비용보다 큰 경우
      # 현재 카드를 책상에 놓고 check를 v로 변경한다.
      heapq.heappush(card, check)
      check = v
  return res # 정답 반환

def main():
  N = int(input())
  card = sorted([int(input()) for _ in range(N)])
  print(solution(N, card)) # 정답 출력

if __name__ == "__main__":
  main()