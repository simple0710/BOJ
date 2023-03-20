# 2023/03/20 Implementation
# https://www.acmicpc.net/problem/5566
N, M = map(int,input().split())
board = [0] * (N + 1)
for i in range(N): # 보드 데이터 저장
  board[i+1] = int(input())

res = -1
s = 1
for cnt in range(M): # 주사위 굴리기
  s += int(input())
  if s >= N or s + board[s] >= N: # 목표에 도착한 경우
    if res == -1:
      res = cnt + 1
    continue
  s += board[s]
# 정답 출력
print(res)