# 2023/11/15 Implementation, Bruteforcing
# https://www.acmicpc.net/problem/17281
from itertools import permutations
import sys
input = sys.stdin.readline

# 이닝 수
N = int(input())
# 이닝 결과 목록
inning_list = [list(map(int,input().split())) for _ in range(N)]
res = 0
for rotation in permutations(range(1, 9)):
  rotation = [0] + list(rotation)
  turn = 5 # 첫 선수는 4번 타자 고정
  score = 0
  for inning in inning_list: # 경기 시작
    board = [0] * 4
    out_cnt = 0
    while out_cnt < 3: # 3회 아웃시 종료
      turn = (turn + 1) % 9 # 다음 타자
      now = inning[rotation[turn]] # 현재 타자가 공을 친 결과
      if now == 0: # 아웃
        out_cnt += 1
      elif now == 1: # 안타
        score += board[3]
        board = [0, 1, board[1], board[2]]
      elif now == 2: # 2루타
        score += board[2] + board[3]
        board = [0, 0, 1, board[1]]
      elif now == 3: # 3루타
        score += board[1] + board[2] + board[3]
        board = [0, 0, 0, 1]
      elif now == 4: # 홈런
        score += board[1] + board[2] + board[3] + 1
        board = [0, 0, 0, 0]
  # 최대 점수 갱신
  res = max(res, score)
# 최대 점수 출력
print(res)