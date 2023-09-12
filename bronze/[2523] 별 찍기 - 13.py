# 2023/09/10 Impelmentation
# https://www.acmicpc.net/problem/2523
N = int(input())
# 별 출력
for i in range(1,N+1):
  print('*'*i)
for i in range(N-1):
  print('*'*(N-1-i))