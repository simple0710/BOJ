# 2023/07/11 Math, BinarySearch
# https://www.acmicpc.net/problem/13706
def binary_search():
  s = 0
  e = N
  while s <= e:
    mid = (s + e) // 2
    if mid ** 2 == N: # N과 같은 경우 mid 반환
      return mid
    elif mid ** 2 < N: # N보다 작은 경우
      s = mid + 1
    else: # N보다 큰 경우
      e = mid - 1
N = int(input())
# 탐색 후 정답 출력
print(binary_search())