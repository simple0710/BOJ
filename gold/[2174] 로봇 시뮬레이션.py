# 2023/10/08 Implementation, Simulation
# https://www.acmicpc.net/problem/2174
import sys
input = sys.stdin.readline

# A가로
# B세로
# x 가로 -> 세로
# y 세로 -> 가로
def solution(A, B, N, M, r_start, commands):
  direction = {'N' : 0, 'E' : 1, 'S' : 2, 'W' : 3}
  dx = [1, 0, -1, 0]
  dy = [0, 1, 0, -1]

  # 데이터 저장
  board = [[-1] * (A+1) for _ in range(B+1)]
  robots = dict()
  for idx, (x, y, d) in enumerate(r_start):
    board[x][y] = idx+1
    robots[idx+1] = [x, y, direction[d]]

  # 명령 시작
  for number, command, reapeat in commands:
    x, y, d = robots[number]
    if command == 'F': # 앞으로 한 칸 이동
      board[x][y] = -1
      for _ in range(reapeat): # 반복 횟수만큼 이동
        x += dx[d]
        y += dy[d]
        if x < 1 or x > B or y < 1 or y > A: # 벽에 부딪힌 경우
          return f'Robot {number} crashes into the wall'
        if board[x][y] != -1: # 이동 중, 다른 로봇이 있는 경우
          return f'Robot {number} crashes into robot {board[x][y]}'
      # 이동한 위치 저장
      robots[number] = [x, y, d]
      board[x][y] = number
    else: # 방향 회전
      t = 1 if command == 'R' else -1
      nd = (d + t * reapeat) % 4
      robots[number][2] = nd
  return 'OK' # 잘못된 명령이 없는 경우

def main():
  A, B = map(int,input().split())
  N, M = map(int,input().split())
  r_start = []
  for _ in range(N):
    x, y, d = input().rstrip().split()
    r_start.append((int(y), int(x), d))
  commands = []
  for _ in range(M):
    n, c, r = input().rstrip().split()
    commands.append((int(n), c, int(r)))
  print(solution(A, B, N, M, r_start, commands)) # 정답 출력

if __name__ == "__main__":
  main()