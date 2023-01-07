# 2022/12/25 DP
# https://www.acmicpc.net/problem/11054
N = int(input())
data = list(map(int,input().split()))
reverse_data = data[::-1]
dp1 = [1] * N
dp2 = [1] * N
res = [0] * N

for i in range(N):
  for j in range(i):
    # 가장 긴 증가하는 순열
    if data[i] > data[j]:
      dp1[i] = max(dp1[i], dp1[j] + 1)
    # 가장 긴 감소하는 순열
    if reverse_data[i] > reverse_data[j]:
      dp2[i] = max(dp2[i], dp2[j] + 1)

for i in range(N):
  res[i] = dp1[i] + dp2[N-i-1] - 1 # 리버스한 값이므로 N-i-1

# 정답 출력
print(max(res))