# 2023/05/13 BinarySearch
# https://www.acmicpc.net/problem/14627
import sys
input = sys.stdin.readline

def binary_search():
  s = 1
  e = max(data)
  res = 0
  while s <= e:
    mid = (s + e) // 2
    cnt = 0
    check = 0
    for i in data: # 만들 수 있는 파닭의 수와 나머지 계산
      cnt += i // mid
      check += i % mid
    if cnt >= C: # 파닭의 개수가 C보다 크거나 같은 경우
      if cnt > C: # 파닭의 개수가 C보다 더 큰 경우
        check += (cnt - C) * mid
      res = check
      s = mid + 1
    else: # 파닭의 개수가 C보다 작은 경우
      e = mid - 1
  # 정답 출력
  print(res)

N, C = map(int, input().split())
data = [int(input()) for _ in range(N)]
# 탐색 시작
binary_search()