# 2023/04/13 TwoPointer
# https://www.acmicpc.net/problem/1484
def two_pointer():
  s = 2
  e = 1
  res = []
  while True:
    check = s**2 - e**2
    if s == e:
      break
    if G >= check: # check보다 G가 더 크거나 같은 경우
      if G == check:
        res.append(s)
      s += 1
    else: # check가 G보다 작은 경우
      e += 1
  # 정답 출력
  if res:
    for i in res:
      print(i)
  else:
    print(-1)

G = int(input())
# 탐색 시작
two_pointer()