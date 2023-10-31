# 2023/08/18 Combinatorics, Hash-Set
# https://www.acmicpc.net/problem/9375
from collections import defaultdict
import sys
input = sys.stdin.readline

def solution(data):
  res = 1
  for i in data.values():
    # +1은 해당 의상을 착용하지 않은 경우를 포함한 것이다.
    res *= i + 1
  return res - 1

def main():
  T = int(input())
  for _ in range(T):
    N = int(input())
    data = defaultdict(int)
    for _ in range(N):
      wear = input().rstrip().split()
      data[wear[1]] += 1
    print(solution(data))

if __name__ == "__main__":
  main()