# 2023/04/16 Math, Greedy
# https://www.acmicpc.net/problem/27961
N = int(input())
if N == 0: # 고양이를 키울 생각이 없는 경우
  print(0)
else: # 생각이 있는 경우
  c = 1
  cnt = 1
  while c < N: # N을 초과한 경우 종료
    c *= 2
    cnt += 1
  # 정답 출력
  print(cnt)