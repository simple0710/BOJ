# 2023/03/16 Implementation
# https://www.acmicpc.net/problem/10810
N, M = map(int,input().split())
basket = [0] * (N+1)
for _ in range(M):
  i, j, k = map(int,input().split())
  for v in range(i, j+1): # 공 채우기
    basket[v] = k
# 정답 출력
print(' '.join(map(str, basket[1:])))