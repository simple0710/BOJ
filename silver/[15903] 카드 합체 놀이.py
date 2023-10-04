# 2023/10/04 Greedy, PriorityQueue
# https://www.acmicpc.net/problem/15903
import sys, heapq
input = sys.stdin.readline

def solution(M, card):
  heapq.heapify(card) # 리스트 -> heapq 변환
  for _ in range(M):
    v = 0
    for _ in range(2): # 가장 작은 두 카드의 더한 값 계산
      v += heapq.heappop(card)
    for _ in range(2): # 덮어 씌우기
      heapq.heappush(card, v)
  return sum(card) # 모든 카드의 합 반환

def main():
  N, M = map(int,input().split())
  card = list(map(int,input().split()))
  print(solution(M, card)) # 정답 출력

if __name__ == "__main__":
  main()