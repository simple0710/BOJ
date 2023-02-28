# 2023/02/28 수학
# https://www.acmicpc.net/problem/5063
# 어느게 이득인지만 알면 된다.
for _ in range(int(input())):
  r, e, c = map(int,input().split())
  # 정답 출력
  if r < (e - c):
    print("advertise")
  elif r == (e-c):
    print("does not matter")
  else:
    print("do not advertise")