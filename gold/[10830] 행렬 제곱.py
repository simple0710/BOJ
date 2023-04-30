# 2023/04/30 Math, LinearAlgebra, DivideAndConquer, ExponentiationBySquaring
# https://www.acmicpc.net/problem/10830
import sys
input = sys.stdin.readline

def mul(a, b): # 행렬 곱하기
  check = [[0] * N for _ in range(N)]
  for i in range(N):
    for j in range(N):
      for k in range(N):
        check[i][j] += a[i][k] * b[k][j]
      check[i][j] %= 1000
  return check # 계산 값 반환

def sol(b):
  if b == 1: # 1의 제곱인 경우
    return A
  elif b == 2: # 2의 제곱인 경우
    return mul(A, A)
  else: # 그 이상인 경우
    tmp = sol(b // 2)
    if b % 2 == 0: # b가 짝수 4인 경우 AAAA이므로 tmp * tmp를 하면 된다.
      return mul(tmp, tmp)
    else: # b가 홀수 5인 경우 AAAAA이므로 tmp * tmp * A로 계산한다.
      return mul(mul(tmp, tmp), A)

N, B = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
# 탐색 시작
res = sol(B)
# 정답 출력
for i in res:
  for j in i:
    print(j % 1000, end=' ')
  print()