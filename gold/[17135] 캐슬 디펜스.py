# 2023/01/05 그래프, 브루투포스
# https://www.acmicpc.net/problem/17135
from collections import deque
import sys, copy
input = sys.stdin.readline

# 순서 조합
def dfs(sy, s):
  global res
  if len(s) == 3:
    res = max(res, play(s, data))
    return
      
  for i in range(sy, M):
    if (N, i) not in s:
      s.append((N, i))
      dfs(i, s)
      s.pop()

# main(병사 확인, 제거, 하단 이동, 남은 병사확인)
def play(s, data):
  ndata = copy.deepcopy(data)
  nenemy = deque(reversed(enemy))
  cnt = 0
  while True:
    e = set()
    # 병사 확인
    for x, y in s:
      a = search(x, y, nenemy)
      if a:
        e.add(a)

    # 병사 제거
    for x, y in e:
      ndata[x][y] = 0
      cnt += 1

    # 병사들을 한칸씩 내리기
    for _ in range(len(nenemy)):
      x, y = nenemy.popleft()
      if ndata[x][y]:
        ndata[x][y] = 0
        if x+1 < N:
          ndata[x+1][y] = 1
          nenemy.append((x+1, y))

    # 남은 병사 확인
    check = 0
    for i in ndata:
      check += i.count(1)
    if not check:
      return cnt

# 사정거리 안의 병사 확인
def search(x, y, nenemy):
  dist = int(1e9)
  flag = 0
  # 타겟이 겹치더라도, 가장 왼쪽에 있는 병사를 사격한다.
  for nx, ny in nenemy:
    tmp = abs(x-nx) + abs(y-ny)
    if tmp <= D:
      flag = 1
      if dist > tmp:
        tx, ty = nx, ny
        dist = tmp
      elif dist == tmp:
        if ny < ty:
          tx, ty = nx, ny
      else:
        pass
  if flag:
    return tx, ty

if __name__=="__main__":
  N, M, D = map(int,input().split())
  enemy = []
  data = []
  for i in range(N):
    data.append(list(map(int,input().split())))
    for j in range(M):
      # 병사 정보 수집
      if data[i][j]:
        enemy.append((i, j))

  dx = [0, -1, 0]
  dy = [-1, 0, 1]
  res = 0
  s = []

  # 탐색 시작(순서 조합 → 게임 시작 → 종료)
  dfs(0, s)

  # 정답 출력
  print(res)