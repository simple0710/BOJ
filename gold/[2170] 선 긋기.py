# 2022/12/01 정렬, 스위핑
# https://www.acmicpc.net/problem/2170
import sys
input = sys.stdin.readline

# 정보 입력
data = []
N = int(input())
for _ in range(N):
  x, y = map(int, input().split())
  data.append((x, y))

# 정렬
data.sort(key = lambda x : x[0])
e = -int(1e9) - 1
res = 0

# 데이터 전부를 확인한다.
for x, y in data:
  if e <= x: # 현재 끝 길이보다 x가 같거나 큰 경우
    res += y - x # 겹치는 경우
  else:
    # 끝 부분이 현재 끝 부분보다 긴 경우
    if e < y:
      # 늘어난 만큼만 더한다.
      res += y - e
  # 끝 값을 큰 수로 바꾼다.
  e = max(e, y)

# 정답 출력
print(res)