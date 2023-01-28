# 2023/01/28 BruteForce
# https://www.acmicpc.net/problem/2531
import sys
input = sys.stdin.readline

N, d, k, c = map(int,input().split())
# 초밥 정보 입력
cho_list = []
for _ in range(N):
  cho = int(input())
  cho_list.append(cho)

# 탐색 시작
res = 0
for i in range(N):
  # 연속된 초밥을 먹는 경우 확인
  if i + k <= N:
    check = set(list(cho_list[i:i+k]))
  else:
    check = set(list(cho_list[i:N]) + cho_list[0: (i+k) % N])
  p = len(check)
  if c not in check: # 먹은 것 중 쿠폰에 적힌 번호가 없는 경우 +1
     p += 1
  res = max(res, p)

# 정답 출력
print(res)
