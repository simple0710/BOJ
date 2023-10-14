# 2023/09/16 Implementation, Simulation
# https://www.acmicpc.net/problem/30036
from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 잉크 칠하기
# x, y지점을 기점으로 cnt거리안에 있는 장애물을 c색으로 칠한다.
def ink_spread(x, y, cnt, c):
  global stage

  visited = [[-1] * N for _ in range(N)]
  q = deque([(x, y)])
  visited[x][y] = 0
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
        if visited[x][y] + 1 <= cnt:
          visited[nx][ny] = visited[x][y] + 1
          q.append((nx, ny))
          if stage[nx][ny] != '.': # 이미 칠해졌거나, 장애물인 경우
            stage[nx][ny] = c

def solution():
  global stage
  moves = {'U': (-1, 0), 'D': (1, 0), 'L' : (0, -1), 'R' : (0, 1)}
  ink_cnt = 0
  jump_cnt = 0
  for i in range(N):
    for j in range(N):
      if stage[i][j] == '@': # 현재 위치 확인
        stage[i][j] = '.'
        x, y = i, j

  for i in command:
    if i == 'j': # 잉크 충전
      ink_cnt += 1
    elif i == 'J': # 점프
      jump_cnt += 1
      # t * I + d번째 점프할 때의 잉크의 색상이 d번째 문자가 된다는 의미는
      # (t * I + d) % I이고, 결국 d % I번 문자가 된다는 의미이다.
      ink_spread(x, y, ink_cnt, ink_string[(jump_cnt-1) % I])
      ink_cnt = 0 # 잉크 초기화
    else: # 이동
      nx = x + moves[i][0]
      ny = y + moves[i][1]
      # 움직일 수 있는 영역으로 이동
      if 0 <= nx < N and 0 <= ny < N and stage[nx][ny] == '.':
        x = nx
        y = ny
  # 현재 위치 저장
  stage[x][y] = '@'
  for i in stage: # 정답 출력
    print(''.join(i))

def main():
  global I, N, K, ink_string, stage, command

  I, N, K = map(int,input().split())
  ink_string = input().rstrip()
  stage = [list(input().rstrip()) for _ in range(N)]
  command = input().rstrip()
  solution() # 탐색 시작

if __name__ == "__main__":
  main()