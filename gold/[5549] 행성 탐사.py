# 2023/03/30 Prefix Sum
# https://www.acmicpc.net/problem/5549
from collections import defaultdict
import sys
input = sys.stdin.readline

M, N = map(int,input().split())
K = int(input())
data = [list(input().rstrip()) for _ in range(M)]
pre = [[defaultdict(int) for _ in range(N+1)] for _ in range(M+1)]
# 누적합 계산하기
for i in range(1, M+1):
  for j in range(1, N+1):
    for k in "JOI": 
      # 왼쪽 직사각형 + 위쪽 직사각형 - 좌측 상단 직사각형
      pre[i][j][k] += pre[i-1][j][k]
      pre[i][j][k] += pre[i][j-1][k]
      pre[i][j][k] -= pre[i-1][j-1][k]
    pre[i][j][data[i-1][j-1]] += 1 # 현재 값 더하기

for _ in range(K):
  a, b, c, d = map(int,input().split())
  # 정답 출력
  for k in "JOI":
    print(pre[c][d][k] + pre[a-1][b-1][k] - pre[c][b-1][k] - pre[a-1][d][k], end=' ')
  print()