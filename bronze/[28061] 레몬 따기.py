# 2023/05/23 Math
# https://www.acmicpc.net/problem/28061
N = int(input())
data = list(map(int,input().split()))
res = 0
for i in range(N):
  check = data[i] - (N - i)
  res = max(res, check) # 값 비교
# 정답 출력
print(res)