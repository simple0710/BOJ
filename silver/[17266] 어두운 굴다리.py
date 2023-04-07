# 2023/04/07 BinarySearch
# https://www.acmicpc.net/problem/17266
def binary_search():
  s = max(data[0], N - data[-1])
  e = 100000
  res = 100000
  while s <= e:
    mid = (s + e) // 2
    # 가로등 확인
    for i in range(1, M):
      if (data[i] - data[i-1]) / 2 > mid:
        s = mid + 1
        break
    else:
      res = min(res, mid)
      e = mid - 1
  # 정답 반환
  return res

N = int(input())
M = int(input())
data = list(map(int,input().split()))
# 탐색 후 정답 출력
print(binary_search())