# 2022/11/21 DP
# i-j**2 지역을 확인하고 이용할 수 있는 값에 +1을 하여 가장 작은 값을 찾는다.
import sys
input = sys.stdin.readline

# 입력
N = int(input())

# 정보 입력
dp = [i for i in range (N+1)]

# 시작
for i in range(1 , N + 1):
  for j in range(1, i):
    # j**2이 i보다 크면 종료
    if (j**2) > i:
      break
    # dp[i-j**2] + 1이 dp[i] 보다 작다면 값을 수정한다
    if dp[i] > dp[i - j**2] + 1:
      dp[i] = dp[i - j**2] + 1

# 정답 출력
print(dp[N])