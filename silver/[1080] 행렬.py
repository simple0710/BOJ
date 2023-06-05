# 2023/06/05 Greedy
# https://www.acmicpc.net/problem/1080
def check(x, y): # 배열 뒤집기
  for i in range(x, x + 3):
    for j in range(y, y + 3):
      data_a[i][j] = not data_a[i][j]

N, M = map(int,input().split())
data_a = [list(map(int,input().rstrip())) for _ in range(N)]
data_b = [list(map(int,input().rstrip())) for _ in range(N)]
res = 0
if (N < 3 or M < 3) and data_a != data_b: # 뒤집을 수 없는 경우
  res = -1
else:
  for i in range(N-2):
    for j in range(M-2):
      if data_a[i][j] != data_b[i][j]: # 해당 칸이 같지 않은 경운
        res += 1
        check(i, j)
  if data_a != data_b: # 뒤집어도 같지 않은 경우
    res = -1
# 정답 출력    
print(res)