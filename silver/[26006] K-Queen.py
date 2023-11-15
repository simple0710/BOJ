# 2023/09/05 Implementation
# https://www.acmicpc.net/problem/26006
import sys
input = sys.stdin.readline
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def solution():
  white_area = set([(wx, wy)])
  # 하얀 킹의 구역 추가
  for i in range(8):
    nx = wx + dx[i]
    ny = wy + dy[i]
    if 0 < nx <= N and 0 < ny <= N:
      white_area.add((nx, ny))
  # 검은 퀸
  for x, y in black:
    check = set()
    for cx, cy in white_area:
      # 행, 열, 대각선에 존재하는 경우
      if x == cx or y == cy or abs(cx - x) == abs(cy - y):
        check.add((cx, cy))
    white_area = white_area - check
  if (wx, wy) not in white_area: # 현재 위치를 잡힌 경우
    if white_area: # 이동할 구역이 있는 경우
      return "CHECK"
    else: # 이동할 구역이 없는 경우
      return "CHECKMATE"
  else: # 현재 위치에 있을 수 있는 경우
    if len(white_area) == 1: # 현재 위치에만 있는 경우
      return "STALEMATE"
  return "NONE" # 아무 일도 없는 경우

if __name__ == "__main__":
  N, K = map(int,input().split())
  wx, wy = map(int,input().split())
  black = [list(map(int,input().split())) for _ in range(K)]
  print(solution()) # 정답 출력