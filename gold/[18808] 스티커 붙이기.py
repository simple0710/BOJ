# 2023/11/20 Implementation, Simulation, Bruteforcing
# https://www.acmicpc.net/problem/18808
import sys
input = sys.stdin.readline

# 스티커 시계방향 90도 회전
def sticker_turn(sticker):
  return list(zip(*sticker[::-1]))

# 붙일 수 있는 구역 확인
def paint_check(board, now, sticker_info):
  r, c, sticker = sticker_info
  x, y = now
  for i in range(x, x + r):
    for j in range(y, y + c):
      # 스티커가 겹치는 경우 False 반환
      if board[i][j] and sticker[i-x][j-y]: return False
  # 스티커가 겹치지 않는 경우 True 반환
  return True

# 스티커 붙이기
def paint(board, now, sticker_info):
  r, c, sticker = sticker_info
  x, y = now
  for i in range(x, x + r):
    for j in range(y, y + c):
      board[i][j] = sticker[i-x][j-y] | board[i][j]

# 구역 탐색
def search_place(board, N, M, sticker_info):
  r, c, sticker = sticker_info
  for x in range(N):
    for y in range(M):
      if x + r <= N and y + c <= M: # 스티커를 붙일 만한 공간이 있는 경우
        # 스티커를 붙일 수 있는 경우
        if paint_check(board, (x, y), sticker_info):
          # 스티커 붙이기
          paint(board, (x, y), sticker_info)
          return True
  # 스티커를 붙이지 못한 경우
  return False

def solution(N, M, K, stickers):
  board = [[0] * M for _ in range(N)]
  for sticker_info in stickers:
    r, c, now_sticker = sticker_info
    for _ in range(4):
      # 붙일 수 있는 구역이 있는 경우 현재 스티커 차례 종료
      if search_place(board, N, M, (r, c, now_sticker)): break
      # 스티커 시계방향으로 90도 회전
      now_sticker = sticker_turn(now_sticker)
      r, c = c, r

  # 스티커가 붙은 칸의 수 확인
  res = 0
  for i in board: res += i.count(1)
  return res # 스티커가 붙은 칸의 수 반환
        
def main():
  # 세로 길이, 가로 길이, 스티커의 개수
  N, M, K = map(int,input().split())
  # 스티커 정보 입력
  stickers = []
  for _ in range(K):
    R, C = map(int,input().split())
    sticker = [list(map(int,input().split())) for _ in range(R)]
    stickers.append((R, C, sticker))
  print(solution(N, M, K, stickers)) # 스티커가 붙은 칸의 수 출력

if __name__ == "__main__":
  main()