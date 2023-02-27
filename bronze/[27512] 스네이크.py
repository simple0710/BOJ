# 2023/02/27
# https://www.acmicpc.net/problem/27512
n, m = map(int,input().split())
res = n * m
# 모든 칸의 수가 홀수인 경우
if n*m % 2 != 0:
  res -= 1
# 정답 출력
print(res)