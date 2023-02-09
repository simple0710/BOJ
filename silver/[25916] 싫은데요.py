# 2023/02/09 두 포인터
# https://www.acmicpc.net/problem/25916
import sys
input = sys.stdin.readline

# 두 포인터를 이용한다.
def search():
  res = 0
  start = 0
  end = 1
  s = arr[0]
  while end < N: # 끝 부분에 도착한 경우 종료
    if s + arr[end] <= M: # 최대 영역 보다 낮은 경우 end += 1
      s += arr[end]
      end += 1
      res = max(res, s)
    else: # 최대 영역 보다 큰 경우 start += 1
      s -= arr[start]
      start += 1
  return res

N, M = map(int,input().split())
arr = list(map(int,input().split()))

# 탐색 시작
res = search()

# 정답 출력
print(res)