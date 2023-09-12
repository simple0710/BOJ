# 2023/06/17 Math
# https://www.acmicpc.net/problem/28236
import sys
N, M, K = map(int,input().split())
res = 1
length = sys.maxsize
for i in range(K):
  a, b = map(int,input().split())
  # 오른쪽 하단이 목적지이므로 N - (N - a)이다.
  if length > abs(N - (N - a)) + abs(M - b):
    res = i + 1
    length = abs(N - (N - a)) + abs(M - b)
print(res) # 정답 출력