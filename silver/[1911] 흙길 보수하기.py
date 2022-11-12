# 2022/11/12 그리디 알고리즘
# 정보 입력
N, L = map(int,input().split())
data = []
for _ in range(N):
  s, e = map(int,input().split())
  data.append([s, e])
data.sort(key = lambda x : x[0])

board = data[0][0]
res = 0
for s, e in data:
  # 이미 판자로 덮혀진 경우는 스킵
  if board > e:
    continue
  # 현재 위치가 시작지점보다 작다면 값 변경
  elif board < s:
    board = s
  # 거리 측정
  dist = e - board
  r = 1
  # 판자를 알뜰히 쓴 경우
  if dist % L == 0:
    r = 0
  # 쓴 판자의 수
  cnt = dist // L + r
  # 현재 위치 에서 쓴 판자수 만큼 이동
  board += cnt * L
  # 쓴 판자 수를 res에 더함
  res += cnt
# 정답 출력
print(res)