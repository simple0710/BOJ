# 2023/03/22 Implementation
# https://www.acmicpc.net/problem/1652
import sys
input = sys.stdin.readline

def search(v):
  c = 0
  r = 0
  c_flag = 0
  r_flag = 0
  for i in range(N): # 가로 확인
    if room[v][i] == '.':
      c += 1
    else:
      c = 0
    if room[i][v] == '.': # 세로 확인
      r += 1
    else:
      r = 0
    if c == 2:
      c_flag += 1
    if r == 2:
      r_flag += 1
  # 누울 수 있는 곳 반환
  return (r_flag, c_flag)

N = int(input())
room = [list(input().rstrip()) for _ in range(N)]
res_c = 0
res_r = 0
for i in range(N):
  # 탐색 시작
  a, b = search(i)
  res_r += a
  res_c += b 
# 정답 출력
print(res_c, res_r)