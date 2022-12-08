# 2022/11/30 누적 합, 에라토스테네스의 채
# https://www.acmicpc.net/problem/17425
MAX = int(1e6)

dp = [1] * (MAX+1) # 약수의 합 저장
s = [0] * (MAX+1) # 누적합 저장
# 해당 소수를 가지는 수를 dp[N]에 저장한다.
for i in range(2, MAX+1):
  j = 1
  while i*j <= MAX:
    dp[i*j] += i
    j += 1

# 누적합 저장
for i in range(1, MAX+1):
  s[i] = s[i-1] + dp[i]

n = int(input())
res = []
for _ in range(n):
  tmp = int(input())
  res.append(s[tmp])

# 정답 출력
print('\n'.join(map(str, res)))