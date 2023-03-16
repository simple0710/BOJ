# 2023/03/16 Implementation
# https://www.acmicpc.net/problem/2476
res = 0
for _ in range(int(input())):
  a, b, c = map(int,input().split())
  if a == b and b == c: # 같은 눈이 3개인 경우
    p = 10000 + (a * 1000)
  elif a != b and b != c and a != c: # 같은 눈이 없는 경우
    p = max(a, b, c) * 100
  else: # 같은 눈이 2개인 경우
    if a == b:
      p = 1000 + (a * 100)
    else:
      p = 1000 + (c * 100)
  res = max(res, p) # 최대 값 갱신
# 정답 출력
print(res)