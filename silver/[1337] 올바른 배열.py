# 2023/04/11 Implementation, Sorting
# https://www.acmicpc.net/problem/1337
N = int(input())
data = sorted(list(int(input()) for _ in range(N)))
res = 4
for i in range(N-1):
  check = 1
  for j in range(i+1, min(i+5, N)): # 다음 4개의 수 확인
    if data[j] - data[i] < 5:
      check += 1
  # 정답 계산
  res = min(res, 5 - check)
# 정답 출력
print(res)