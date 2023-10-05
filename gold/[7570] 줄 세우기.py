# 2023/10/05 Greedy, DP
# https://www.acmicpc.net/problem/7570
import sys
input = sys.stdin.readline

def solution(N, children):
  # 1씩 증가하는 가장 긴 수열을 찾는다.
  # 해당 수열에 포함되지 않은 번호를 한 쪽 방향으로 이동 시킨다.
  dp = [0] * (N+1)
  length = 0
  for i in children:
    dp[i] = dp[i-1] + 1
    length = max(dp[i], length)
  return N-length # 이동 횟수 반환

def main():
  N = int(input())
  children = list(map(int,input().split()))
  print(solution(N, children)) # 정답 출력

if __name__ == "__main__":
  main()