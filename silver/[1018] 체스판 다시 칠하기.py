# 2023/04/01 BruteForce
# https://www.acmicpc.net/problem/1018
import sys
input = sys.stdin.readline

def search(x, y):
  ny = 0
  w_value = 0
  b_value = 1
  w = 0
  b = 0
  for i in range(x, x + 8):
    for j in range(y, y + 8):
      # 검사할 보드를 변경해가며 확인해본다.
      if data[i][j] != board_check[w_value][ny]:
        w += 1
      if data[i][j] != board_check[b_value][ny]:
        b += 1
      ny += 1
    ny = 0
    w_value = (w_value + 1) % 2
    b_value = (b_value + 1) % 2
  # 작은 값 반환
  return min(w, b)

N, M = map(int,input().split())
data = [list(input().rstrip()) for _ in range(N)]
board_check = [['W', 'B'] * 4, ['B', 'W'] * 4]

res = sys.maxsize
for i in range(7, N):
  for j in range(7, M):
    # 왼쪽 상단부터 탐색 시작
    res = min(res, search(i-7, j-7))
# 정답 출력
print(res)