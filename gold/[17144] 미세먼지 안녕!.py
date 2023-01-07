# 2022/12/16 구현
# https://www.acmicpc.net/problem/17144
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def clean():
  global data
  for _ in range(T):
    new_data = [[0] * M for _ in range(N)]
    for i in range(N):
      for j in range(M):
        if (i, j) in cleaner:
          new_data[i][j] = -1
        elif data[i][j] > 0:
          dust_move(i, j, new_data)
        else:
          pass
    for idx, (x, y) in enumerate(cleaner):
      tmp = 0
      for ny in range(y+1, M): # 오른쪽 이동
        pre_value = new_data[x][ny]
        new_data[x][ny] = tmp
        tmp = pre_value
      # 위쪽 공기 청정기
      if idx == 0:
        for nx in range(x-1, -1, -1):
          pre_value = new_data[nx][M-1]
          new_data[nx][M-1] = tmp
          tmp = pre_value
        for ny in range(M-2, -1, -1):
          pre_value = new_data[0][ny]
          new_data[0][ny] = tmp
          tmp = pre_value
        for nx in range(1, x):
          pre_value = new_data[nx][0]
          new_data[nx][0] = tmp
          tmp = pre_value
      # 아래쪽 공기 청정기
      elif idx == 1:
        for nx in range(x+1, N):
          pre_value = new_data[nx][M-1]
          new_data[nx][M-1] = tmp
          tmp = pre_value
        for ny in range(M-2, -1, -1):
          pre_value = new_data[N-1][ny]
          new_data[N-1][ny] = tmp
          tmp = pre_value
        for nx in range(N-2, x, -1):
          pre_value = new_data[nx][0]
          new_data[nx][0] = tmp
          tmp = pre_value
      else:
        pass
    data = new_data
  res = 0
  for i in data:
    res += sum(i)
  # 결과 출력
  print(res + 2)

# 먼지 움직이기
def dust_move(x, y, new_data):
  turn = 0
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < N and 0 <= ny < M and data[nx][ny] != -1:
      new_data[nx][ny] += data[x][y] // 5
      turn += 1
  new_data[x][y] += data[x][y] - (data[x][y] // 5) * turn

if __name__ == "__main__":
  N, M, T = map(int,input().split())
  data = []
  cleaner = []
  for i in range(N):
    data.append(list(map(int,input().split())))
    for j in range(M):
      # 공기 청정기 위치 저장
      if data[i][j] == -1:
        cleaner.append((i, j))
  # 청정기 시작
  clean()