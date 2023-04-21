# 2023/04/21 Implementation
# https://www.acmicpc.net/problem/2576
n = []
for i in range(7):
  a = int(input())
  if a % 2 != 0: # 홀수인 경우
    n.append(a) # 배열에 추가
if n: # 홀수가 있는 경우
  print(sum(n))
  print(min(n))
else: # 홀수가 없는 경우
  print(-1)