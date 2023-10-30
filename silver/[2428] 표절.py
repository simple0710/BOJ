# 2023/07/16 BinarySearch, Sorting
# https://www.acmicpc.net/problem/2428
import sys
input = sys.stdin.readline

def bianry_search(number): # 이진 탐색 수행
  s = i
  e = N - 1
  check = 0
  while s <= e:
    mid = (s + e) // 2
    # 조건 내인 경우
    if data[mid] * 0.9 <= number:
      s = mid + 1
      check = max(check, mid)
    else: # 조건을 벗어난 경우
     e = mid - 1
  return check - i # 범위 반환

N = int(input())
data = sorted(list(map(int,input().split())))
res = 0
for i in range(N):
  res += bianry_search(data[i])
# 정답 출력
print(res)