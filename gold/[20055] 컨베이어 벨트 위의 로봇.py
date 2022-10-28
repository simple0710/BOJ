from collections import deque
N, K = map(int,input().split())
arr = list(map(int,input().split()))
robot = dict()
c = 1
time = 1
change = -1
while True:
  # 1 단계
  arr.insert(0, arr.pop(-1))
  for i in robot:
    robot[i] = (robot[i] + 1) % (2*N)
    if robot[i] == N-1:
      change = i
  if change != -1:
    del robot[change]
    change = -1

  # 2 단계
  for i in robot:
    move_robot = (robot[i] + 1) % (2*N)
    if arr[move_robot] and move_robot not in robot.values():
      robot[i] = move_robot
      arr[move_robot] -= 1
      if robot[i] == N-1:
        change = i
  if change != -1:
    del robot[change]
    change = -1

  # 3 단계
  if arr[0] and int(0) not in robot.values():
    robot[c] = 0
    c += 1
    arr[0] -= 1

  # 4 단계
  if arr.count(0) >= K:
    break
  time += 1

print(time)