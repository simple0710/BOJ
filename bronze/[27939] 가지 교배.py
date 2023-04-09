# 2023/04/08 Implementation
# https://www.acmicpc.net/problem/27939
N = int(input())
data = list(input().split())
m, k = map(int, input().split())
res = 'P'
for _ in range(m):
  check = list(map(int,input().split()))
  w_check = 0
  p_check = 0
  for i in check: # 흰색, 보라색 체크
    if data[i-1] == 'W':
      w_check += 1
    else:
      p_check += 1
  if w_check >= 1 and p_check == 0: # 흰색만 가지고 있다면 답은 W
    res = 'W'
# 정답 출력
print(res)