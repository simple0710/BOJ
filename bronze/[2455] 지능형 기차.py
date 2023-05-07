# 2023/05/07 Implementation, Math
# https://www.acmicpc.net/problem/2455
res = 0
now = 0
for _ in range(4):
  a, b = map(int,input().split())
  now += b - a # 현재 승객
  res = max(res, now) # 최대 승객
# 정답 출력
print(res)