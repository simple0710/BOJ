# 2023/10/23 DP
# https://www.acmicpc.net/problem/17485
import sys
input = sys.stdin.readline
MAX = sys.maxsize

def solution(N, M, arr):
  dp = [[[0] * M for _ in range(N+1)] for _ in range(3)]
  for i in range(1, N+1): 
    for j in range(M):
      # 오른쪽, 이전에 오른쪽을 지나온 경우는 제외한다.
      dp[0][i][j] = min(dp[1][i-1][j-1], dp[2][i-1][j-1]) + arr[i-1][j-1] if j > 0 else MAX
      # 중간, 이전에 중간을 지나온 경우는 제외한다.
      dp[1][i][j] = min(dp[0][i-1][j], dp[2][i-1][j]) + arr[i-1][j]
      # 왼쪽, 이전에 왼쪽을 지나온 경우는 제외한다.
      dp[2][i][j] = min(dp[0][i-1][j+1], dp[1][i-1][j+1]) + arr[i-1][j+1] if j < M-1 else MAX
  res = min([min(dp[k][-1]) for k in range(3)]) # 마지막 결과 확인
  return res # 연료의 최솟값 반환

def main():
  # 행렬의 크기
  N, M = map(int,input().split())
  # 행렬의 원소 값(N행, M열)
  arr = [list(map(int,input().split())) for _ in range(N)]
  print(solution(N, M, arr)) # 연료의 최솟값 출력

if __name__ == "__main__":
  main()