# 2023/08/12 Implementation, Simulation
# https://www.acmicpc.net/problem/28457
import sys
input = sys.stdin.readline

N, S, W, G = map(int,input().split())
golden_card = []
for _ in range(G):
  golden_card.append(list(map(int,input().split())))

board = [0] * (4 * N - 4)
board[3 * N - 3] ='U' # 우주 여행 칸
board[2 * N - 2] ='B' # 사회복지기금 칸
board[N - 1] ='M' # 무인도 칸
board[0] ='S' # 시작 칸
# 특수 칸을 제외한 경우를 확인한다.
res = 0
for i in range(4 * N - 4):
  if not board[i]:
    city_info = input().split()
    if city_info[0] == 'L': # 땅인 경우 땅의 개수 추가
      res += 1
    board[i] = city_info # 게임 판에 땅 혹은 황금 열쇠 정보 저장

# 게임 시작
np = 0
welfare = 0
card_pick_cnt = 0
m_cnt = 0
flag = True
I = int(input())
for i in range(I):
  x, y = map(int,input().split())
  if m_cnt != 0: # 무인도일 경우
    if x == y: # 주사위의 값이 같으면 탈출, 다음 턴에 이동한다.
      m_cnt = 0
    else: # 주사위의 값이 다르면 턴 증가, 머무른다.
      m_cnt -= 1
    continue
  np += x + y # 이동
  if np >= 4 * N - 4: # 월급
    # 월급을 두 번 받을 수 있는 경우가 있다.
    S += W * (np // (4 * N - 4))
    np %= 4 * N - 4

  if board[np][0] == 'G': # 황금 카드
    t = golden_card[card_pick_cnt][0]
    m = int(golden_card[card_pick_cnt][1])
    # 황금 카드의 타입에 따른 행동을 수행한다.
    if t == 1: # 은행에서 m원을 받는다.
      S += m
    elif t == 2: # 은행에 m원을 준다.
      S -= m
    elif t == 3: # 사회복지기금에 m원을 기부한다.
      S -= m
      welfare += m
    elif t == 4: # 앞으로 m칸 이동한다.
      np += m
      if np >= 4 * N - 4: # 시작 지점을 거친 경우
        # 월급 받기
        S += W * (np // (4 * N - 4))
        np %= 4 * N - 4
    card_pick_cnt = (card_pick_cnt + 1) % G # 카드 순서 갱신
    if S < 0: # 자금이 0미만인 경우 패배 확정
      flag = False
  if board[np][0] == 'L': # 땅인 경우
    if S >= int(board[np][1]): # 땅을 살 수 있는 경우
      # 금액 지불 및 땅 구입 확인
      S -= int(board[np][1])
      board[np] = 'X'
      res -= 1
  elif board[np][0] == 'M': # 무인도 칸인 경우
    m_cnt = 3 # 같은 주사위가 나올 때까지 대기 시간 저장
  elif board[np][0] == 'B': # 사회복지기금 칸인 경우
    # 복지기금을 전부 받는다.
    S += welfare
    welfare = 0
  elif board[np][0] == 'U': # 우주
    # 시작 칸으로 이동 후 월급을 받는다.
    np = 0
    S += W
if flag and res == 0: # 자금이 0미만이었던 적이 없고, 모든 땅을 다 산 경우
  print("WIN")
else: # 그 외의 경우
  print("LOSE")