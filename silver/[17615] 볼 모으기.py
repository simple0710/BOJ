# 2022/12/17 그리디
# https://www.acmicpc.net/problem/17615
# 1. 양쪽 끝에 붙어있는 볼의 개수를 구한 뒤 총합에서 뺀다.
# 2. red, blue의 값과 비교해서 작은 값을 정답으로 한다.
N = int(input())
arr = list(input())
red = arr.count('R')
blue = arr.count('B')

# 왼쪽에서 색상과 개수를 확인한다.
l_color = arr[0]
lcnt = 0
for i in range(N):
  if l_color == arr[i]:
    lcnt += 1
  else:
    break

# 오른쪽에서 색상과 개수를 확인한다.
r_color = arr[N-1]
rcnt = 0
for i in range(N-1, -1, -1):
  if r_color == arr[i]:
    rcnt += 1
  else:
    break

# 해당 색상 - lcnt
if l_color == 'R':
  res1 = red - lcnt
else:
  res1 = blue - lcnt
# 해당 색상 - rcnt
if r_color == 'R':
  res2 = red - rcnt
else:
  res2 = blue - rcnt

# 만약 볼의 값이 더 작다면 볼의 값을 정답으로 한다.
if min(res1, res2) > min(red, blue):
  res = min(red, blue)
else:
  res = min(res1, res2)

# 정답 출력
print(res)