# 2023/04/26 Implementation
# https://www.acmicpc.net/problem/11098
for _ in range(int(input())):
  res = -1
  for _ in range(int(input())):
    C, name = input().split() # 가격과 이름
    if res < int(C): # 더 높은 가격의 선수인 경우
      res = int(C)
      res_name = name
  # 정답 출력
  print(res_name)