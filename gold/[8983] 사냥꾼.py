# 2023/04/09 BinarySearch, Sorting
# https://www.acmicpc.net/problem/8983
def binary_search(a, b):
  s = 0
  e = M - 1
  while s <= e:
    mid = (s + e) // 2
    if abs(s_data[mid] - a) + b <= L: # 사거리 안인 경우
      return 1
    else: # 범위 밖인 경우 탐색 재개
      if s_data[mid] - a < 0:
        s = mid + 1
      else:
        e = mid - 1
  return 0

M, N, L = map(int, input().split())
s_data = sorted(list(map(int,input().split())))
animal = sorted([list(map(int,input().split())) for _ in range(N)])
res = 0
# 탐색 시작
for a, b in animal:
  res += binary_search(a, b)
# 정답 출력
print(res)