# 2023/03/25 Implementation
# https://www.acmicpc.net/problem/9506
while True:
  n = int(input())
  if n == -1: # 종료 조건
    break
  data = []
  # 값 구하기
  for i in range(1, n//2+1):
    if n % i == 0:
      data.append(i)
  # 정답 출력
  if n == sum(data):
    print(n, '=', ' + '.join(map(str, data)))
  else:
    print(n, 'is NOT perfect.')
