# 2023/07/05 Math
# https://www.acmicpc.net/problem/1247
for _ in range(3):
  check = 0
  for _ in range(int(input())): # 수의 개수
    check += int(input())
  if check < 0: # 음수인 경우
    print('-')
  elif check == 0: # 0인 경우
    print(0)
  else: # 양수인 경우
    print('+')