# 2023/05/08 TwoPointer
# https://www.acmicpc.net/problem/2018
def two_pointer():
  s = 0
  e = 0
  check = 0
  res = 0
  while e <= N:
    if check <= N: # 값이 N보다 작거나 같은 경우
      if check == N: # 값이 같으면 res + 1
        res += 1
      e += 1
      check += e
    else: # 값이 N보다 큰 경우
      s += 1
      check -= s
  # 정답 출력
  print(res)

N = int(input())
# 탐색 시작
two_pointer()