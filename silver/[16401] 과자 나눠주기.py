# 2023/04/22 BinarySearch
# https://www.acmicpc.net/problem/16401
def binary_search():
  res = 0
  s = 1
  e = max(data)
  while s <= e:
    mid = (s + e) // 2
    # 과자를 mid만큼 나누었을 때의 값 check를 구한다.
    check = 0
    for i in data:
      check += i // mid
    
    if check >= M: # 나누어 줄 수 있는 경우
      s = mid + 1
      res = max(res, mid)
    else: # 나누어 줄 수 없는 경우
      e = mid - 1
  # 정답 반환
  return res

M, N = map(int,input().split())
data = list(map(int,input().split()))
# 탐색 시작
res = binary_search()
# 정답 출력
print(res)