# 2023/02/26 구현
# https://www.acmicpc.net/problem/3009
x = []
y = []
for _ in range(3):
  a, b = map(int,input().split())
  x.append(a)
  y.append(b)

# 하나 밖에 없는 것이 정답이 된다.
if x.count(min(x)) == 1:
  rx = min(x)
else:
  rx = max(x)
if y.count(min(y)) == 1:
  ry = min(y)
else:
  ry = max(y)

# 정답 출력
print(rx, ry)