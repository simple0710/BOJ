# 2023/03/19 Implementation
# https://www.acmicpc.net/problem/10812
N, M = map(int,input().split())
basket = [i for i in range(N+1)]
for _ in range(M):
  i, j, k = map(int,input().split())
  # 바구니 순서 변경
  nb = basket[i:j+1][k-i:] + basket[i:j+1][:k-i]
  for v in range(i, j+1): # 바구니 값 변경
    basket[v] = nb[v-i]
# 정답 출력
print(' '.join(map(str, basket[1:])))
