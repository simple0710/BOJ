# 2023/02/25 구현
# https://www.acmicpc.net/problem/9610
res = {"Q1": 0, "Q2": 0, "Q3": 0, "Q4": 0, "AXIS": 0}
for _ in range(int(input())):
  x, y = map(int,input().split())
  # 사분면에 대한 조건
  if x == 0 or y == 0:
    res["AXIS"] += 1
  elif x > 0 and y > 0:
    res["Q1"] += 1
  elif x < 0 and y > 0:
    res["Q2"] += 1
  elif x < 0 and y < 0:
    res["Q3"] += 1
  else:
    res["Q4"] += 1

# 정답 출력
for key in res.keys():
  print(f"{key}: {res[key]}")