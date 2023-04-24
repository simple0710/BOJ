# 2023/04/24 BinarySearch
# https://www.acmicpc.net/problem/13702
def binary_search():
  s = 1
  e = max(data)
  res = 0
  while s <= e:
    mid = (s + e) // 2
    check = 0
    for i in data:
      check += i // mid
    if check >= K: # 인원 수만큼 분배가 가능할 때
      s = mid + 1
      res = max(res, mid)
    else: # 인원 수만큼 분배가 불가능 할 때
      e = mid - 1
  # 정답 반환
  return res

N, K = map(int,input().split())
data = list(int(input()) for _ in range(N))
# 탐색 시작
res = binary_search()
# 정답 출력
print(res)