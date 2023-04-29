# 2023/04/29 TwoPointer
# https://www.acmicpc.net/problem/22945
def two_pointer():
  s = 0
  e = N - 1
  res = 0
  while s < e:
    check = (e - s - 1) * min(data[s], data[e]) # 합
    if data[s] < data[e]: # 낮은 위치의 인덱스를 이동시킨다.
      s += 1
    else:
      e -= 1
    res = max(res, check)
  # 정답 출력
  print(res)

N = int(input())
data = list(map(int,input().split()))
# 탐색 시작
two_pointer()