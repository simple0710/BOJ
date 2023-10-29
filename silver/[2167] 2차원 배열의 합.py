# 2023/07/21 PrefixSum
# https://www.acmicpc.net/problem/2167
N, M = map(int,input().split())
data = [[0] * (M + 1)]
for i in range(1, N + 1):
  data.append([0] + list(map(int,input().split())))
  for j in range(1, M + 1):
    # 누적합 계산
    data[i][j] += data[i][j-1] + data[i-1][j] - data[i-1][j-1]
# 누적합 정답 출력
for i, j, x, y in list(map(int,input().split()) for _ in range(int(input()))):
    print(data[x][y] - data[x][j-1] - data[i-1][y] + data[i-1][j-1])