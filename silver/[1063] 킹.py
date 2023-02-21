# 2023/02/21 구현
# https://www.acmicpc.net/problem/1063
import sys
input = sys.stdin.readline

# 움직이는 방향에 대한 정의
move = {
  'R' : (0, 1),
  'L' : (0, -1),
  'B' : (-1, 0),
  'T' : (1, 0),
  'RT' : (1, 1),
  'LT' : (1, -1),
  'RB' : (-1, 1),
  'LB' : (-1, -1)
  }

K, S, N = map(str, input().rstrip().split())
kx, ky = int(K[1]), ord(K[0]) - 64 # 킹
sx, sy = int(S[1]), ord(S[0]) - 64 # 돌

for _ in range(int(N)):
  move_type = input().rstrip() # 움직이는 방향 입력
  nkx = kx + move[move_type][0]
  nky = ky + move[move_type][1]
  if 1 <= nkx <= 8 and 1 <= nky <= 8: # 범위 내로 움직일 수 있는 경우
    if nkx == sx and nky == sy:  # 해당 위치에 돌이 있는 경우
      nsx = sx + move[move_type][0]
      nsy = sy + move[move_type][1]
      if 1 <= nsx <= 8 and 1 <= nsy <= 8: # 이동한 돌의 위치가 체스판의 내부인 경우
        sx = nsx
        sy = nsy
        kx = nkx
        ky = nky
    else: # 돌이 없는 경우
      kx = nkx
      ky = nky

# 정답 출력
print(f'{chr(ky+64)}{kx}') # 킹의 위치
print(f'{chr(sy+64)}{sx}') # 돌의 위치