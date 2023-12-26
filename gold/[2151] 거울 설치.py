# 2023/12/26 BFS
# https://www.acmicpc.net/problem/2151
from collections import deque

def solution(N, home, door):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  start, end = door
  q = deque([start])
  visited = [[int(1e9)] * N for _ in range(N)]
  visited[start[0]][start[1]] = 0
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx, ny = x, y
      while True:
        nx += dx[i]
        ny += dy[i]
        # 영역을 벗어나거나 빛이 통과할 수 없는 벽을 만난 경우 종료
        if 0 > nx or N <= nx or 0 > ny or N <= ny or home[nx][ny] == '*':
          break
        # 거울의 위치를 발견한 경우 이전에 사용한 거울 개수가 더 적다면 값 갱신 및 새로 추가
        if home[nx][ny] == '!' and visited[nx][ny] > visited[x][y] + 1:
          q.append((nx, ny))
          visited[nx][ny] = visited[x][y] + 1
        # 다른 쪽 문을 방문한 경우 작은 값으로 값을 갱신한다.
        if home[nx][ny] == '#':
          visited[nx][ny] = min(visited[nx][ny], visited[x][y])
  # 설치해야 할 거울의 최소 개수 반환
  return visited[end[0]][end[1]]

def main():
  N = int(input())
  home = []
  door = []
  for i in range(N):
    home.append(list(input()))
    for j in range(N):
      # 문의 위치 저장
      if home[i][j] == '#': door.append((i, j))
  # 설치해야 할 거울의 최소 개수 출력
  print(solution(N, home, door))

if __name__ == "__main__":
  main()