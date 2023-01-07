# 2022/12/17 비트마스킹
# https://www.acmicpc.net/problem/11811
N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]
res = [0] * N

for i in range(N):
  for j in range(N):
    if i == j:
      continue
    # or 연산을 한 결과를 정답으로 가진다.
    res[i] = res[i] | data[i][j]

# 정답 출력
print(*res)