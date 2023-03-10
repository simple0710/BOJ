# 2023/03/10 Sliding window
# https://www.acmicpc.net/problem/10025
import sys
input = sys.stdin.readline

def search():
  bucket_keys = sorted(list(bucket.keys())) # 좌표 값
  check = [] # 좌표값을 저장한다.
  res = 0 # 얼음들의 합을 갱신한다.
  ans = 0 # 최종 결과
  s = 0 # key의 인덱스
  for x in range(max(bucket_keys) + 1):
    # 현재 위치 안에 있는 양동이가 있는 경우
    while s < N and bucket_keys[s] <= x + K:
      res += bucket[bucket_keys[s]]
      check.append(bucket_keys[s])
      s += 1
    # 현재 위치 밖에 양동이가 있는 경우
    while check and check[0] < x - K:
      res -= bucket[check[0]]
      check.pop(0)
    ans = max(ans, res)
  return ans # 정답 반환

N, K = map(int,input().split())
bucket = dict()
for _ in range(N):
  V, D = map(int,input().split())
  bucket[D] = V

# 탐색 시작
res = search()

# 정답 출력
print(res)