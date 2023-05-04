# 2023/05/04 TwoPointer
# https://www.acmicpc.net/problem/26091
def two_pointer():
  res = 0
  s = 0
  e = N - 1
  while s < e:
    if data[s] + data[e] >= M: # 두 합이 M이상인 경우
      res += 1
      s += 1
      e -= 1
    else: # 가장 작은 값 증가
      s += 1
  # 정답 출력
  print(res)

N, M = map(int,input().split())
data = sorted(list(map(int,input().split())))
# 탐색 시작
two_pointer()