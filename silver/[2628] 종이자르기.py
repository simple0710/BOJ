# 2023/07/06 Sorting
# https://www.acmicpc.net/problem/2628
N, M = map(int,input().split())
rows = [0, N]
cols = [0, M]
for _ in range(int(input())):
  direction, line = map(int, input().split())
  if direction == 0: # 방향에 맞는 배열에 추가
    cols.append(line)
  else:
    rows.append(line)

# 배열 정렬
cols.sort()
rows.sort()

# 가장 큰 가로와 세로의 넓이를 구한다.
check_r = []
check_c = []
for i in range(1, len(cols)):
  check_c.append(cols[i] - cols[i-1])
for i in range(1, len(rows)):
  check_r.append(rows[i] - rows[i-1])
# 정답 출력
print(max(check_c) * max(check_r))