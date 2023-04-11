# 2023/04/12 TwoPointer
# https://www.acmicpc.net/problem/4158
import sys
input = sys.stdin.readline

def two_pointer():
  ns = 0
  ms = 0
  res = 0
  while ns < N and ms < M:
    if n_data[ns] == m_data[ms]: # CD 번호가 같은 경우
      res += 1
    if ns == N - 1: # n이 끝에 도달한 경우
      ms += 1
    elif ms == M - 1: # m이 끝에 도달한 경우
      ns += 1
    else:
      if n_data[ns] < m_data[ms]:
        ns += 1
      else:
        ms += 1
  # 정답 출력
  print(res)

while True:
  N, M = map(int,input().split())
  if N == M == 0:
    break
  n_data = list(int(input()) for _ in range(N))
  m_data = list(int(input()) for _ in range(M))
  # 탐색 시작
  two_pointer()