# 2022/12/31 DP
# https://www.acmicpc.net/problem/11066
# dp[0][2]는 0부터 2까지 더해서 나타날 수 있는 최솟값이다.
import sys
input = sys.stdin.readline

for _ in range(int(input())):
  N = int(input())
  arr = list(map(int, input().split()))
  dp = [[0] * (N+1) for _ in range(N+1)]
  for i in range(N-1):
    # 대각선으로 움직인다.
    dp[i][i+1] = arr[i] + arr[i+1] # 해당 위치의 파일 합쳐보기
    for j in range(i+2, N): # 합친 파일을 포함한 합
      dp[i][j] = dp[i][j-1] + arr[j]

  for i in range(2, N):
    for j in range(N-i):
      k = i + j
      # min은 이전 값, M은 중간 지점
      dp[j][k] += min([dp[j][M] + dp[M+1][k] for M in range(j, k)]) 
  
  print(dp[0][N-1])