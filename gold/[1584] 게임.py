# 2023/12/10 0-1 BFS
# https://www.acmicpc.net/problem/1584
from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(danger_area, death_area):
  q = deque([(0, 0, 0)])
  visited = set([(0, 0)])
  while q:
    x, y, life = q.popleft()
    # 목적지에 도착한 경우 생명 반환
    if (x, y) == (500, 500): return life
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 영역을 벗어나지 않고, 방문한 적이 없는 경우 확인
      if 0 <= nx <= 500 and 0 <= ny <= 500 and (nx, ny) not in visited:
        visited.add((nx, ny))
        # 죽음의 구역 확인
        for x1, y1, x2, y2 in death_area:
          if min(x1, x2) <= nx <= max(x1, x2) and min(y1, y2) <= ny <= max(y1, y2): break
        else: # 죽음의 구역에 속하지 않은 경우
          # 위험한 구역 확인
          for x1, y1, x2, y2 in danger_area:
            # 위험한 구역인 경우 후순위로 추가
            if min(x1, x2) <= nx <= max(x1, x2) and min(y1, y2) <= ny <= max(y1, y2):
              q.append((nx, ny, life+1))
              break
          # 위험한 구역이 아닌 경우 우선순위로 추가
          else: q.appendleft((nx, ny, life))
  return -1 # 목적지에 도착할 수 없는 경우 -1 반환

def main():
  N = int(input())
  danger_area = [list(map(int,input().split())) for _ in range(N)]
  M = int(input())
  death_area = [list(map(int,input().split())) for _ in range(M)]
  print(solution(danger_area, death_area)) # 생명의 최솟값 출력

if __name__ == "__main__":
  main()