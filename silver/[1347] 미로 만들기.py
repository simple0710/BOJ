# 2023/01/15 구현
# https://www.acmicpc.net/problem/1347
N = int(input())
arr = input()
res = [['.']]
d = 1 # 남쪽
x, y = 0, 0 # 시작 위치
h, w = 1, 1 # 지도의 크기

# 움직이기
for i in arr:
  d %= 4
  if i == 'R': # 오른쪽 회전
    d -= 1
  elif i == 'L': # 왼쪽 회전
    d += 1
  elif i == 'F': # 앞으로 이동
    if d == 0: # 서
      if y - 1 < 0:
        w += 1
        for i in res:
          i.insert(0, '#')
      else:
        y -= 1
    elif d == 1: # 남
      if x + 1 >= h:
        h += 1
        res.append(['#'] * w)
      x += 1
    elif d == 2: # 동
      if y + 1 >= w:
        w += 1
        for i in res:
          i.append('#')
      y += 1
    elif d == 3: # 북
      if x - 1 < 0:
        h += 1
        res.insert(0, ['#'] * w)
      else:
        x -= 1
    res[x][y] = '.'

# 정답 출력
for i in res:
  print(''.join(map(str, i)))