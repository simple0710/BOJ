# 2023/08/14 DP
# https://www.acmicpc.net/problem/28706
import sys
input = sys.stdin.readline

for _ in range(int(input())):
  N = int(input())
  dp = [[0] * 7 for _ in range(N + 1)]
  dp[0][1] = True # 시작점
  for i in range(1, N + 1):
    a, b, c, d = map(str,input().split())
    b = int(b)
    d = int(d)
    for x in range(7): # 0에서 6까지 확인한다.
      if dp[i-1][x]: # x인 경우가 나온 경우
        xb = (x + b if a == '+' else x * b) % 7 
        xd = (x + d if c == '+' else x * d) % 7 
        dp[i][xb] = True 
        dp[i][xd] = True
  if dp[-1][0]: # 7의 배수가 된 경우
    print("LUCKY")
  else: # 7의 배수가 될 수 없는 경우
    print("UNLUCKY")