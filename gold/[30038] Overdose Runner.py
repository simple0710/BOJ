# 2023/09/17 Implementation, Simulation
# https://www.acmicpc.net/problem/30038
# 몬스터에 대한 정의는 다음과 같다.
"""
몬스터의 순서는 y 좌표가 같다면 x 좌표가 증가하는 순서대로 
y 좌표가 다르다면 y 좌표가 증가하는 순서대로 출력한다.
"""
# 평범하게 n만큼 몬스터가 있을 때, 가장 낮은 x부터 , 가장 낮은 y순으로 몬스터의 번호를 지정한다고 이해하면 된다.
# ex) 1 : (0, 0), 2 : (0, 1), ..., n-1 : (N-1, M-2), n : (N-1, M-1)
import sys
input = sys.stdin.readline
moves = {'u' : (-1, 0), 'd' : (1, 0), 'l' : (0, -1), 'r' : (0, 1)}

# x, y위치에서 command방향으로 투사체를 투척한다.
def monster_attack(x, y, command): # 공격
  total_exp = 0
  for i in range(1, attack_distance+1): # 공격 거리만큼 투사체 투척
    nx = x + moves[command[-1]][0] * i
    ny = y + moves[command[-1]][1] * i
    # 영역을 벗어나거나 장애물인 경우 투사체 삭제
    # 몬스터를 맞혀도 투사체는 통과한다.
    if nx < 0 or nx >= N or ny < 0 or ny >= M or board[nx][ny] == '*':
      break
    if str(board[nx][ny]).isdecimal(): # 몬스터인 경우
      mh, md, mexp = monster_info[board[nx][ny]]
      # 공격력 - 몬스터의 방어력이며, 
      # 몬스터의 방어력이 공격력보다 높디고 해서 체력이 증가하지 않는다.
      mh -= (attack - md) if attack > md else 0
      monster_info[board[nx][ny]] = [mh, md, mexp] # 결과 저장
      if mh <= 0: # 몬스터가 쓰러진 경우
        board[nx][ny] = '.'
        total_exp += mexp # 경험치 획득
  return total_exp # 얻은 경험치 반환

def solution():
  global attack, attack_distance
  # 캐릭터 초기 스탯
  attack = 5
  attack_distance = 1
  speed = 1
  need_exp = 10
  now_exp = 0
  level = 1
  eat_drug = 0
  drug_cnt_check = 0

  mcnt = 0
  for i in range(N):
    for j in range(M):
      if board[i][j] == 'p': # 플레이어 위치 확인
        board[i][j] = '.'
        x, y = i, j
      elif board[i][j] == 'm': # 몬스터 위치 숫자로 저장
        board[i][j] = mcnt
        mcnt += 1

  # 이동의 경우 행동할 수 없다면 행동력(cnt)은 0이 소모된다.
  cnt = 0
  for command in commands:
    if eat_drug > 0 and eat_drug % 5 == 0: # 약을 5번 먹을 때마다 OVERDOSE상태가 된다.
      # 이동, 대기 행동만 가능하며, 행동력을 10이상 소모해야 다른 행동을 할 수 있다.
      if cnt - drug_cnt_check < 10:
        if len(command) == 2 or command == 'c':
          continue
    if command in ['u', 'd', 'l', 'r']: # 순간이동(행동력 1)
      # speed의 위치로 정확히 순간이동한다.
      nx = x + moves[command][0] * speed
      ny = y + moves[command][1] * speed
      # 영역내에서 장애물이 아니고, 몬스터가 아닌 경우 해당 위치로 순간이동
      if 0 <= nx < N and 0 <= ny < M:
        if board[nx][ny] != '*' and not str(board[nx][ny]).isdecimal():
          x = nx
          y = ny
          cnt += 1
    elif command == 'w': # 대기(행동력 1)
      cnt += 1
    elif command in ['au', 'ad', 'al', 'ar']: # 공격(행동력 3)
      cnt += 3
      # 공격 시작
      now_exp += monster_attack(x, y, command)
      while now_exp >= need_exp: # 경험치가 요구 경험치보다 높거나 같은 경우
        level += 1 # 레벨업
        attack += level - 1 # 이전 레벨만큼 공격력 증가
        attack_distance += 1 # 공격 사거리 1 증가
        now_exp -= need_exp
        need_exp += 10 # 요구 경험치 10 증가
    elif command == 'c': # 클리어(행동력 0)
      if board[x][y] == 'g': # 현재 위치가 목적지인 경우 종료
        break
    else: # 약먹기(행동력 2)
      # 속도가 0일때, dd를 수행해도 약을 먹은 판정이다.
      cnt += 2
      eat_drug += 1 
      drug_cnt_check = cnt # 약을 먹었을 당시 행동력
      if command[-1] == 'u': # 속도 증가 약인 경우 속도 증가
        speed += 1
      else: # 속도 감소 약인 경우 속도 감소
        speed -= 1
        if speed < 0: # 0미만으로 떨어지지 않는다.
          speed = 0

  # --출력 목록--
  # 레벨, 경험치
  # 소모 행동력
  # 모든 행동이 끝난 후 게임판의 상태
  # 남아있는 몬스터의 체력을 공백으로 구분하여 출력(몬스터가 있는 경우)
  print(level, now_exp)
  print(cnt)
  board[x][y] = 'p'
  monster_cnt = 0
  mh = [] # 몬스터 체력 리스트
  for i in range(N):
    for j in range(M):
      if str(board[i][j]).isdecimal(): # 몬스터가 있는 경우
        mh.append(monster_info[board[i][j]][0])
        board[i][j] = 'm' # 문자 변경
        monster_cnt += 1
    # 게임판 출력
    print(''.join(map(str, board[i])))
  if monster_cnt: # 몬스터가 남아있는 경우 체력 출력
    for i in range(len(mh)):
      print(mh[i], end = ' ')

if __name__ == '__main__':
  N, M = map(int,input().split())
  # 게임판
  board = [list(input().rstrip()) for _ in range(N)]
  k = int(input())
  # 체력, 방어력, 획득 경험치
  mh = list(map(int,input().split()))
  md = list(map(int,input().split()))
  mexp = list(map(int,input().split()))
  # 몬스터 정보
  monster_info = [[mh[i], md[i], mexp[i]] for i in range(k)]
  s = int(input())
  # 행동 리스트
  commands = list(input().rstrip().split())
  solution() # 게임 실행