# 2023/07/30 BinarySearch
# https://www.acmicpc.net/problem/15732
import sys
input = sys.stdin.readline
def bianry_search():
  s = 1
  e = N
  while s <= e:
    mid = (s + e) // 2 # 끝 부분을 mid로 하고 이진 탐색을 수행한다.
    check = 0
    for first, last, term in rules: # 규칙을 확인한다.
      if first > mid: # 범위 밖인 경우
        continue
      if mid > last: # mid가 last보다 더 큰 경우
        check += ((last - first) // term + 1)
      else: # last가 mid와 같거나 더 큰 경우
        check += ((mid - first) // term + 1)
      if check >= D: # D이상인 경우 e = mid - 1 및 정답 저장
        e = mid - 1
        res = mid
        break
    else: # D이상이 되지 못한 경우
      s = mid + 1
  return res # 정답 반환

N, K, D = map(int,input().split())
rules = []
for _ in range(K):
  rules.append(list(map(int,input().split())))
print(bianry_search()) # 탐색 및 정답 출력