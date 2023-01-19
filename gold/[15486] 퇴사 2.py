# 2023/01/19 DP
# https://www.acmicpc.net/problem/15486
import sys
input = sys.stdin.readline

N = int(input())
data = [0] * N
dp = [0] * (N+1)
# 데이터 저장
for i in range(N):
  t, p = map(int,input().split())
  data[i] = (t, p)

# 맨 뒤에서 부터 시작한다.
for i in range(N-1, -1, -1):
  if i + data[i][0] > N: # 날짜를 넘어가는 경우 이전 값을 가져온다.
    dp[i] = dp[i+1]
  else: # 일을 하지 않은 경우와 일을 한 경우를 비교한다.
    dp[i] = max(data[i][1] + dp[i + data[i][0]], dp[i + 1])

# 정답 출력
print(dp[0])