# 2023/06/17 Math, Bruteforcing
# https://www.acmicpc.net/problem/28242
import sys
input = sys.stdin.readline

def find(number):
  number = abs(number)
  check_list = []
  for i in range(1, number + 1):
    if i * (number // i) == number: # 해당 자리에 맞는 수와 같은 경우
      check_list.append((i, number // i))
  if (number // 2) ** 2 == number: # 절반으로 나눈 값이 현재 값과 같은 경우
    check_list.append((number // 2, number // 2))
  return check_list # 리스트 반환

N = int(input())
# n^2 + (n+1) * x - (n + 2)
# 첫번째, 두번째, 세번째
f = N
s = N + 1
t = -(N + 2)
# 첫번째에 올 수 있는 경우를 구한다(a, b)
first = find(f)
# 세번째에 올 수 있는 경우를 구한다(a, b)
last = find(t)
res = False
# 첫번째 경우와, 세번째 경우롤 합쳐 탐색한다.
for i in first:
  for j in last:
    # 계산한 뒤 s와 같으면 정답이 된다.
    if i[0] * j[1] + i[1] * -j[0] == s:
      res = i[0], -j[0], i[1], j[1]
# 정답 출력
if res:
  print(*res)
else:
  print(-1)