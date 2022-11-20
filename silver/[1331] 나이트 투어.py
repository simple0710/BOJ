# 2022/11/20 구현, 시뮬레이션
# 움직임을 저장하는 q 생성
q = []
for _ in range(36):
  m = input()
  # 아스키 코드를 통한 값을 저장
  q.append((ord(m[0])-65, int(m[1]) - 1))

# 방문 기록과 움직일 수 있는 경우의 수 추가
visited = [[False] * 6 for _ in range(6)]
moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, -1), (2, 1), (-2, -1), (-2, 1)]

s = q.pop(0) # 시작 위치 지정
q.append(s) # 골인 지점 지정
stx = s[0]
sty = s[1]
res = "Valid"

# 시작
while q:
  flag = 0
  x, y = q.pop(0)
  for move in moves:
    nx = stx + move[0]
    ny = sty + move[1]
    # 해당 위치로 이동해보고 방문하지 않은 경우
    # 자신의 위치 변경 및 방문처리
    if nx == x and ny == y and not visited[nx][ny]:
      stx = nx
      sty = ny
      visited[nx][ny] = True
      flag = 1
      break
  # 이전 경우가 한번도 없는 경우 "Invalid" 출력
  if flag == 0:
    res = "Invalid"

# 방문하지 못한 지역이 있는 경우 "Invalid" 출력
for i in visited:
  if i.count(False) > 0:
    res = "Invalid"

# 정답 출력
print(res)