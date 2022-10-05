import sys
input = sys.stdin.readline

# 백트래킹
def sdk(idx):
  # 0의 수와 길이가 같다면 출력
  if idx == len(b):
    for i in data:
      print(*i)
    # 종료를 하지 않을 경우 시간 초과
    exit(0)

  for i in range(1, 10):
    x = b[idx][0]
    y = b[idx][1]
    # 모든 조건에 부합한 경우
    if check_col(x, i) and check_row(y, i) and check_square(x, y, i):
      data[x][y] = i
      sdk(idx+1)
      data[x][y] = 0

# 행을 확인한다.
def check_col(x, a):
  if a in data[x][0:]:
    return False
  return True

# 열을 확인한다.
def check_row(y, a):
  if a in [dr[y] for dr in data]:
    return False
  return True

# 3 * 3 칸을 확인한다.
def check_square(x, y, a):
  x_square = x // 3 * 3
  y_square = y // 3 * 3
  for i in range(3):
    for j in range(3):
      if a == data[x_square + i][y_square + j]:
        return False
  return True

# 데이터 입력
data = [list(map(int,input().rstrip().split())) for _ in range(9)]
b = list()
for i in range(9):
  for j in range(9):
    if data[i][j] == 0:
      b.append((i, j))

sdk(0)
