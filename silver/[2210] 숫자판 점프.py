# 2023/03/07 dfs
# https://www.acmicpc.net/problem/2210
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, depth, word):
  # 길이가 5인 경우
  if depth == 5:
    global res
    # res에 추가하고 종료
    res.add(word)
    return
  
  for i in range(4): # 4방향을 돌아본다.
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < 5 and 0 <= ny < 5:
      nword = data[nx][ny] + word
      dfs(nx, ny, depth+1, nword)

data = [list(map(str,input().rstrip().split())) for _ in range(5)]
res = set()
for i in range(5):
  for j in range(5):
    # 위치, 깊이, 숫자
    dfs(i, j, 0, data[i][j])

# 정답 출력
print(len(res))