# 2023/04/04 BinarySearch
# https://www.acmicpc.net/problem/2343
def binary():
  s = 0
  e = sum(data)
  check = sum(data)
  while s <= e:
    mid = (s + e) // 2
    if mid < max(data): # data의 최댓값보다 작으면 계산이 불가능
      s = mid + 1
      continue
    tmp = 0
    cnt = 1
    for i in range(N): # cnt를 구한다.
      if tmp + data[i] <= mid:
        tmp += data[i]
      else:
        cnt += 1
        tmp = data[i]
    # cnt가 M보다 작거나 같으면 e = mid - 1, check를 지정
    if cnt <= M:
      e = mid - 1
      check = min(check, mid)
    else: # cnt가 M보다 큰 경우 s = mid + 1
      s = mid + 1
  # 정답 반환
  return check

N, M = map(int,input().split())
data = list(map(int,input().split()))
# 탐색 시작
res = binary()
# 정답 출력
print(res)