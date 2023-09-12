# 2023/07/14 Implementation
# https://www.acmicpc.net/problem/28289
res = [0] * (4)
for _ in range(int(input())):
  G, C, N = map(int,input().split())
  if G == 1: # 1학년인 경우
    res[3] += 1
  elif C == 1 or C == 2: # 소프트웨어개발과
    res[0] += 1
  elif C == 3: # 임베디드소프트웨어개발과
    res[1] += 1
  else: # 인공지능소프트웨어개발과
    res[2] += 1
for i in res: # 정답 출력
  print(i)