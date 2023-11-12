# 2023/11/12 DataStructures, Sorting, Hash-Set
# https://www.acmicpc.net/problem/11652
from collections import defaultdict
import sys
input = sys.stdin.readline

def solution(N, count):
  max_ = max(count.values())
  # 가장 많이 가지고 있는 수에서 가장 작은 값 반환
  return sorted([i for i in count if count[i] == max_])[0]

def main():
  # 가지고 있는 숫자 카드의 개수
  N = int(input())
  count = defaultdict(int)
  for _ in range(N):
    # 카드에 적혀있는 정수
    count[int(input())] += 1
  # 가장 많이 가지고 있는 정수를 출력
  print(solution(N, count))

if __name__ == "__main__":
  main()