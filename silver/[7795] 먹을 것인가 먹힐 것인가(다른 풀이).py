# 2023/04/05 Sorting, BinarySearch
# https://www.acmicpc.net/problem/7795
def binary_search(v):
  s = 0
  e = M - 1
  check = -1 # 반환 후 +1 되므로 -1로 check 선언
  while s <= e:
    mid = (s + e) // 2
    if B[mid] >= v: # B가 더 크거나 같은 경우
      e = mid - 1
    else:  # A가 더 큰 경우 check 지정
      check = mid
      s = mid + 1
  # check 반환
  return check

for _ in range(int(input())):
  N, M = map(int,input().split())
  A = list(map(int,input().split()))
  B = sorted(list(map(int,input().split())))
  res = 0
  # 탐색 시작
  for i in A:
    res += binary_search(i) + 1
  # 정답 출력
  print(res)