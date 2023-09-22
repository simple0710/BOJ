# 2023/06/13 Implementaion, Bruteforcing, Backtracking
# https://www.acmicpc.net/problem/15684
import sys
input = sys.stdin.readline
def back():
  for i in range(N): # 사다리 이동하기
    sh = i
    for j in range(H):
      if ladder[sh][j] != -1: # 다른 라인으로 이동해야 하는 경우
        sh = ladder[sh][j]
    if sh != i: # 제대로 도착하지 못한 경우
      return False
  # 제대로 도착한 경우
  return True

def ladder_cut(cnt, x, y):
  global res
  if back(): # 번호에 맞게 도착한 경우
    res = min(res, cnt)
  if cnt > 2: # 3이상인 경우 종료
    return
  # 사다리 배치
  for i in range(x, N):
    for j in range(y if i == x else 0, H):
      if ladder[i][j] == -1:
        if i + 1 < N and ladder[i+1][j] == -1:
          ladder[i][j] = i + 1
          ladder[i+1][j] = i
          ladder_cut(cnt + 1, i, j)
          ladder[i][j] = -1
          ladder[i+1][j] = -1
  
N, M, H = map(int,input().split())
ladder = [[-1] * H for _ in range(N)]
for _ in range(M):
  a, b = map(int,input().split()) # 세로번, b + 1번 세로 선을 a와 연결
  # 해당 라인, 포인트 = 이동 위치
  ladder[b-1][a-1] = b
  ladder[b][a-1] = b-1

# 탐색 시작
res = 4
ladder_cut(0, 0, 0)

# 정답 출력
print(res if res != 4 else -1)