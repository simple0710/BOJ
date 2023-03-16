# 2023/03/16 Implementation
# https://www.acmicpc.net/problem/10811
N, M = map(int,input().split())
basket = [i for i in range(N+1)]
for _ in range(M):
  i, j = map(int,input().split())
  for v in basket[i:j+1]: # 역순으로 담기
    basket[j] = v
    j -= 1
# 정답 출력
print(' '.join(map(str, basket[1:])))