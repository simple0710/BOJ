# 2023/03/23 Implementation
# https://www.acmicpc.net/problem/11557
for _ in range(int(input())):
  p = -1
  for _ in range(int(input())):
    a = input().split()
    if p < int(a[1]): # 현재 값보다 큰 경우 res 변경
      p = int(a[1])
      res = a[0]
  # 정답 출력
  print(res)