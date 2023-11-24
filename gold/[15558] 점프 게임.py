# 2023/11/24 BFS
# https://www.acmicpc.net/problem/15558
from collections import deque

def solution(N, K, line):
  # init
  dw = [0, 0, 1]
  dx = [1, -1, K]
  q = deque([(0, 0)])
  visited = [[False] * N for _ in range(2)]
  visited[0][0] = True
  turn = 0
  while q:
    # 현재 턴의 모든 이동 경우 확인
    for _ in range(len(q)):
      w, x = q.popleft()
      if x < turn: # 없어진 칸인 경우
        continue
      for i in range(3):
        nw = (w + dw[i]) % 2
        nx = x + dx[i]
        if nx >= N: # 클리어 가능
          return 1
        # 이동할 수 없는 경우
        # 이동 했었던 경우
        if nx < turn or line[nw][nx] == '0' or visited[nw][nx]:
          continue
        # 이동
        q.append((nw, nx))
        visited[nw][nx] = True
    turn += 1
  return 0 # 클리어 불가능

def main():
  # 칸의 개수, 줄 변경시 이동 거리
  N, K = map(int,input().split())
  # 두 줄의 정보
  line = [list(input()) for _ in range(2)]
  # 클리어 여부 출력
  print(solution(N, K, line))

if __name__ == "__main__":
  main()