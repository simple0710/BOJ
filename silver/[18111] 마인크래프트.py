# 2023/02/08 bruteforce
# https://www.acmicpc.net/problem/18111
import sys
input = sys.stdin.readline

def search(h):
  global res, height
  pb = 0 # 벽을 부술 때 얻는 블록
  mb = 0 # 벽을 만들 때 드는 블록
  # 전 지역 탐색
  for i in range(N):
    for j in range(M):
      if data[i][j] >= h: # 벽 부수기
        pb += data[i][j] - h
      else: # 벽 만들기
        mb += h - data[i][j]
  # 벽을 만드는데 드는 블록보다 남은 블록이 더 많은 경우
  if pb + B >= mb:
    # 결과 비교
    if mb + (pb * 2) <= res:
      res = mb + (pb * 2)
      height = h

N, M, B = map(int,input().split())
data = []
for i in range(N):
  data.append(list(map(int,input().split())))

# 탐색 시작
res = sys.maxsize
height = 0
for i in range(257):
  search(i)

# 정답 출력
print(res, height)