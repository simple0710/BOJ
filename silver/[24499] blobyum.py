# 2023/03/21 Sliding Window
# https://www.acmicpc.net/problem/24499
N, K = map(int,input().split())
arr = list(map(int,input().split()))
s = sum(arr[:K])
res = s
for i in range(K, N + K):
  ni = i % N
  s += arr[ni] # 오른쪽 값 추가
  s -= arr[ni - K] # 왼쪽 값 감소
  res = max(res, s) # 정답 갱신
# 정답 출력
print(res)