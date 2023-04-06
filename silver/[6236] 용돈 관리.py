# 2023/04/06 BinarySearch
# https://www.acmicpc.net/problem/6236
import sys
input = sys.stdin.readline

def binary_search():
  s = max(data)
  e = sum(data)
  res = sum(data)
  while s <= e:
    mid = (s + e) // 2
    check = 0
    cnt = 0
    for i in data:
      if check - i < 0:
        check = mid - i
        cnt += 1
      else:
        check -= i
    if cnt > M: # cnt가 M보다 더 큰 경우
      s = mid + 1
    else: # cnt가 M보다 작은 경우
      res = min(res, mid)
      e = mid - 1
  # 정답 반환
  return res

N, M = map(int,input().split())
data = []
for _ in range(N):
  data.append(int(input()))
# 탐색 시작
res = binary_search()

# 정답 출력
print(res)