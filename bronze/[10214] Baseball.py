# 2023/03/26 Implemetation
# https://www.acmicpc.net/problem/10214
for _ in range(int(input())):
  y, g = 0, 0
  for _ in range(9):
    a, b = map(int,input().split())
    # 득점 더하기
    y += a
    g += b
  # 정답 출력
  if y > g:
    print("Yonsei")
  elif y == g:
    print("Draw")
  else:
    print("Korea")