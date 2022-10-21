from collections import deque

# 기본 상태를 확인한다.
# 같은 극일 경우 움직이지 않는다.
def rotate(gear):
  if gear < num:
    for i in range(gear, num):
      if data[i][2] == data[i+1][6]:
        return 0
  elif gear > num:
    for i in range(gear, num, -1):
      if data[i][6] == data[i-1][2]:
        return 0

data = list()
for _ in range(4):
  a = deque(map(int,input()))
  data.append(a)
  
for _ in range(int(input())):
  num, w = map(int,input().split())
  num -= 1
  if w == 1:
    if num % 2 != 0:
      moves = [-1, 1, -1, 1]
    else:
      moves = [1, -1, 1, -1]
  else:
    if num % 2 != 0:
      moves = [1, -1, 1, -1]
    else:
      moves = [-1, 1, -1, 1]
  # 기어를 돌려보고, 극이 같으면 0 값을 대입한다.
  for i in range(4):
    a = rotate(i)
    if a != None:
      moves[i] = a
  # num은 무조건 움직이므로 따로 추가
  moves[num] = w

  # 움직인다.
  for i in range(4):  
    if moves[i] == 1:
      data[i].appendleft(data[i].pop())
    elif moves[i] == -1:
      data[i].append(data[i].popleft())

# 결과
result = 0
for i in range(4):
  if data[i][0] == 1:
    result += 2**i
print(result)

