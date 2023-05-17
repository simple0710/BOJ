# 2023/05/17 BinarySearch
# https://www.acmicpc.net/problem/15810
def binary_search():
  s = 0
  e = max(data) * M
  res = max(data) * M # 총 시간
  while s <= e:
    mid = (s + e) // 2
    check = 0
    for i in data: # 풍선을 불어본다.
      check += mid // i
    if check >= M: # 풍선의 개수가 M보다 크거나 같은 경우
      res = min(res, mid)
      e = mid - 1
    else: # 풍선의 개수가 M보다 작은 경우
      s = mid + 1
  # 정답 출력
  print(res)

N, M = map(int,input().split())
data = list(map(int,input().split()))
# 탐색 시작
binary_search()