# 2023/07/10 Math, Bruteforcing
# https://www.acmicpc.net/problem/1590
N, T = map(int,input().split())
res = int(1e9)
for _ in range(N):
  s, i, c = map(int,input().split())
  # 탑승할 수 있는 버스를 찾는다,
  for x in range(c):
    check = s + i * x
    if check >= T:
      res = min(res, check-T)
  
if res == int(1e9): # 탑승할 수 없는 경우
  print(-1)
else: # 탑승한 경우
  print(res)