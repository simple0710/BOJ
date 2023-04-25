# 2023/04/25 TwoPointer
# https://www.acmicpc.net/problem/1940
def two_pointer():
  s = 0
  e = N - 1
  res = 0
  while s < e:
    v = data[s] + data[e] # 두 값의 합
    if v <= M: # 구해야 하는 값보다 작거나 같은 경우
      if v == M: # 같으면 res + 1
        res += 1
      s += 1
    else: # 구해야 하는 값보다 큰 경우
      e -= 1
  # 정답 출력
  print(res)

N = int(input())
M = int(input())
data = sorted(list(map(int,input().split())))
# 탐색 시작
two_pointer()