# 2023/07/27 BinarySearch
# https://www.acmicpc.net/problem/18113
import sys
input = sys.stdin.readline

def binary_search():
  s = 1
  e = max(data)
  res = -1
  while s <= e:
    mid = (s + e) // 2
    check = 0
    for i in data:
      if i > K: # K보다 큰 김밥인 경우
        cut = (i - 2 * K if i >= 2 * K else i - K) // mid # 꼬다리 자르기 후 P개로 나누기
        check += cut
    if check >= M: # M개 이상인 경우
      res = max(res, mid)
      s = mid + 1
    else: # M개 미만인 경우
      e = mid - 1
  # 정답 출력
  print(res)
N, K, M = map(int,input().split())
data = [int(input()) for _ in range(N)]
# 탐색 시작
binary_search()