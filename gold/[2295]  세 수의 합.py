# 2023/10/07 DataStructures, Hash-Set
# https://www.acmicpc.net/problem/2295
import sys
input = sys.stdin.readline

def solution(N, nums):
  nums_sum = set()
  # x + y + z = k
  # x + y = k - z

  # 1. x + y
  for x in nums:
    for y in nums:
      nums_sum.add(x + y)
  
  # 2. k - z
  res = {}
  for z in nums:
    for k in nums:
      if (k - z) in nums_sum:
        res[k] = True
  return max(res) # 가장 큰 값 반환

def main():
  N = int(input())
  nums = set([int(input()) for _ in range(N)])
  print(solution(N, nums)) # 정답 출력

if __name__ == "__main__":
  main()