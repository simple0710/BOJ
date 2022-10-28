n, k = map(int,input().split()) # n가지 동전, 목표 k 원
# 동전 정보 입력
arr = []
for _ in range(n):
  arr.append(int(input()))
dp = [0] * (k + 1)
dp[0] = 1

# 각 동전의 경우의 수를 구함
for i in arr:
  # i로 j원을 만드는 경우의 수를 구함
  for j in range(i, k+1):
    dp[j] += dp[j-i]
print(dp[k])