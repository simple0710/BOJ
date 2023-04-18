# 2023/04/17 Implementation, Simulation
# https://www.acmicpc.net/problem/1547
d = [0, 1, 0, 0]
for _ in range(int(input())):
  X, Y = map(int,input().split())
  # 위치 변경
  d[X], d[Y] = d[Y], d[X]
for i in range(len(d)):
  if d[i] == 1: # 공이 있는 경우
    # 정답 출력
    print(i)