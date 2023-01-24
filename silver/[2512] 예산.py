# 2023/01/24 Binary Search
# https://www.acmicpc.net/problem/2512
def search1(): # 0부터 MAX값 까지 찾는 방법
  s = 0
  res = 0
  while True:
    temp = 0
    for i in arr:
      if i < s:
        temp += i
      else:
        temp += s
    if temp <= MAX and s <= max(arr):
      res = max(res, s)
      s += 1
    else:
      return res

def search2(): # binary search
  s = 0
  e = max(arr)
  while s <= e:
    mid = (s + e) // 2
    p = 0
    for i in arr:
      if i < mid:
        p += i
      else:
        p += mid
    if p <= MAX:
      s = mid + 1
    else:
      e = mid - 1
  return e

N = int(input())
arr = sorted(list(map(int,input().split())))
MAX = int(input())
# 정답 출력
print(search2())





