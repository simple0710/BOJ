# 2023/09/10 Implementation
# https://www.acmicpc.net/problem/29738
import sys
input = sys.stdin.readline

def solution():
  # 순위에 따른 라운드를 반환한다.
  if N <= 25: # World Finals에 들어갈 수 있는 순위
    return 'World Finals'
  elif N <= 1000: # Round 3에 들어갈 수 있는 순위
    return "Round 3"
  elif N <= 4500: # Round 2에 들어갈 수 있는 순위
    return "Round 2"
  return "Round 1" # 그 외는 Round 1

if __name__ == "__main__":
  T = int(input())
  for i in range(T):
    N = int(input())
    print(f'Case #{i+1}: {solution()}') # 정답 출력