# 2023/02/24 Greedy
# https://www.acmicpc.net/problem/1789
S = int(input())
N = 1
while True:
  # 1부터 N까지의 합보다 큰 경우
  if ((N*(N+1))//2) > S:
    # 정답 출력
    print(N-1)
    break
  N += 1