def check(row, col, n):
  global blue_cnt, white_cnt
  # 현재 자리의 색깔을 저장한다
  color = data[row][col]
  # n만큼의 범위를 탐색한다.
  for i in range(row, row + n):
    for j in range(col, col + n):
      # 색이 다를 경우 그 자리에서 범위를 절반으로 하고 
      # 모든 색이 같을 때가지 재귀를 수행한다.
      # col + next_n 은 n을 넘을 수 없다.
      if color != data[i][j]:
        next_n = n // 2
        check(row, col, next_n)
        check(row, col + next_n, next_n)
        check(row + next_n, col, next_n)
        check(row + next_n, col + next_n, next_n)
        return
  # 다른 부분이 없었을 때
  # 하얀색일 경우
  if color == 0:
    white_cnt += 1
  # 파란색일 경우
  else:
    blue_cnt += 1
  return
  
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
blue_cnt, white_cnt = 0, 0
check(0, 0, n)
print(white_cnt)
print(blue_cnt)