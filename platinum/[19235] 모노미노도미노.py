# 2023/11/23 Implementation, Simulation
# https://www.acmicpc.net/problem/19235
# 초록색 보드
class GreenBoard:
  def __init__(self):
    self.score = 0
    self.board = [[0] * 4 for _ in range(6)]

  # 블록이 위치할 수 있는 공간 확인
  def check_board_top(self, idx):
    for i in range(6):
      if self.board[i][idx]:
        return i - 1
    return i
  
  # 블록 쌓기
  def stack_board_top(self, idx, t, y):
    # 블록이 위치할 수 있는 가장 높은 공간 확인
    top_x = self.check_board_top(y)
    stack = []
    # 가로 블록인 경우
    if t == 2:
      top_x = min(top_x, self.check_board_top(y+1))
      stack.append((top_x, y+1))
    # 세로 블록인 경우
    if t == 3:
      stack.append((top_x-1, y))
    # 한 칸 쌓기
    stack.append((top_x, y))
    # 모든 공간 쌓기
    for x, y in stack:
      self.board[x] = self.board[x][:]
      self.board[x][y] = idx
  
  # 블록 낙하
  def fall_block(self):
    dx = [0, 0, -1]
    dy = [-1, 1, 0]
    for i in range(4, -1, -1):
      for j in range(4):
        # 블록 존재
        if self.board[i][j]:
          now = i
          idx = self.board[i][j]
          ti, tj = i, j
          # 인접한 블록 확인(좌, 우, 상)
          for dir in range(3):
            ni = i + dx[dir]
            nj = j + dy[dir]
            if 0 <= nj < 4:
              if self.board[i][j] == self.board[ni][nj]:
                ti, tj = ni, nj
          # 최대 낙하 지점까지 확인
          while now < 5:
            if self.board[now+1][j]: # 다음 칸이 블록으로 채워져 있는 경우
              break
            if j != tj: # 같은 열에 위치하는 블록이 아닌 경우
              if self.board[ti+1][tj]: # 해당 블록 다음 칸이 블록으로 채워져 있는 경우
                break
            # 낙하
            self.board[ti][tj] = 0
            self.board[now][j] = 0
            self.board[ti+1][tj] = idx
            self.board[now+1][j] = idx
            now+=1
            ti+=1

  # 점수 증가 확인
  def increase_score(self):
    while True:
      flag = False
      # 모든 블록 확인
      for i in range(2, 6):
        if self.board[i].count(0) == 0: # 모든 행이 채워졌을 때 점수 증가
          self.score += 1
          self.board[i] = [0] * 4 # 블록 제거
          flag = True
      if not flag:
        break
      self.fall_block()

  # 0, 1위치 확인
  def check_over(self):
    cnt = 0
    for i in range(2):
      if self.board[i].count(0) != 4: cnt += 1
    # 0, 1 위치에 블록이 있는 경우 배열 갱신
    if cnt:
      self.board = [[0] * 4] * cnt + self.board[:-cnt]

  def get_score(self): # 점수 반환
    return self.score

  def get_block_cnt(self): # 현재 존재하는 블록 개수 반환
    block_cnt = 0
    for i in self.board: block_cnt += len([v for v in i if v])
    return block_cnt

# 파란색 보드
class BlueBoard:
  def __init__(self):
    self.score = 0
    self.board = [[0] * 6 for _ in range(4)]

  # 블록이 위치할 수 있는 공간 확인
  def check_board_top(self, idx):
    for i in range(6):
      if self.board[idx][i]:
        return i - 1
    return i

  # 블록 쌓기
  def stack_board_top(self, idx, t, x):
    # 블록이 위치할 수 있는 가장 높은 공간 확인
    top_y = self.check_board_top(x)
    stack = []
    # 가로 블록인 경우
    if t == 2:
      stack.append((x, top_y-1))
    # 세로 블록인 경우
    if t == 3:
      top_y = min(top_y, self.check_board_top(x+1))
      stack.append((x+1, top_y))
    # 한 칸 쌓기
    stack.append((x, top_y))
    for x, y in stack:
      self.board[x][y] = idx

  # 블록 낙하
  def fall_block(self):
    dx = [-1, 1, 0]
    dy = [0, 0, -1]
    for i in range(4):
      for j in range(4, -1, -1):
        # 블록 존재
        if self.board[i][j]:
          now = j
          idx = self.board[i][j]
          ti, tj = i, j
          # 인접한 블록 확인(상, 하, 좌)
          for dir in range(3):
            ni = i + dx[dir]
            nj = j + dy[dir]
            if 0 <= ni < 4:
              if self.board[ni][nj] == self.board[i][j]:
                ti, tj = ni, nj
          # 최대 낙하 지점까지 확인
          while now < 5:
            if self.board[i][now+1]: # 다음 칸이 블록으로 채워져 있는 경우
              break
            if i != ti: # 같은 열에 위치하는 블록이 아닌 경우
              if self.board[ti][tj+1]: # 해당 블록 다음 칸이 블록으로 채워져 있는 경우
                break
            # 낙하
            self.board[i][now] = 0
            self.board[ti][tj] = 0
            self.board[i][now+1] = idx
            self.board[ti][tj+1] = idx
            now+=1
            tj+=1

  # 점수 증가 확인
  def increase_score(self):
    flag = True
    while flag:
      flag = False
      for j in range(2, 6):
        # 모든 열이 채워졌을 때 점수 증가
        if len([self.board[i][j] for i in range(4) if self.board[i][j]]) == 4:
          self.score += 1
          for i in range(4): self.board[i][j] = 0 # 블록 제거
          flag = True
      self.fall_block()

  # 0, 1위치 확인
  def check_over(self):
    cnt = 0
    for j in range(2):
      if [self.board[i][j] for i in range(4) if self.board[i][j]]: cnt += 1
    # 0, 1 위치에 블록이 있는 경우 배열 갱신
    if cnt:
      for i in range(4):
        self.board[i] = [0] * cnt + self.board[i][:-cnt]

  def get_score(self): # 점수 반환
    return self.score

  def get_block_cnt(self): # 현재 존재하는 블록 개수 반환
    block_cnt = 0
    for i in self.board: block_cnt += len([v for v in i if v])
    return block_cnt

def solution(block_commands):
  green_board = GreenBoard()
  blue_board = BlueBoard()
  for idx, (t, x, y) in enumerate(block_commands):
    idx += 1
    # 초록색 보드
    green_board.stack_board_top(idx, t, y)
    green_board.increase_score()
    green_board.check_over()
    # 파란색 보드
    blue_board.stack_board_top(idx, t, x)
    blue_board.increase_score()
    blue_board.check_over()
  # 정답 계산
  block_cnt = blue_board.get_block_cnt() + green_board.get_block_cnt()
  total_score = blue_board.get_score() + green_board.get_score()
  print(total_score)
  print(block_cnt)

def main():
  # 명령 개수
  N = int(input())
  # (t, x, y) : 블록 타입, 열, 행
  block_commands = [list(map(int,input().split())) for _ in range(N)]
  solution(block_commands) # 탐색 시작

if __name__ == "__main__":
  main()