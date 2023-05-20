# 2023/05/19 TwoPointer, SlidingWindow
# https://www.acmicpc.net/problem/15565
def two_pointer():
  s = 0
  e = 0
  res = N + 1
  k_check = 1 if data[0] == 1 else 0
  while s < N and e < N :
    if k_check >= K: # K개보다 k_check이 많거나 같거나 큰 경우
      if k_check == K: # 같으면 길이 비교
        res = min(res, e - s + 1)
      if s < N and data[s] == 1: # 라이언 인형인 경우 - 1
        k_check -= 1
      s += 1
    else: # K보다 k_check이 더 작은 경우
      e += 1
      if e < N and data[e] == 1: # 라이언 인형인 경우 + 1
        k_check += 1
  # 정답 출력
  if res == N + 1:
    print(-1)
  else:
    print(res)

N, K = map(int,input().split())
data= list(map(int,input().split()))
two_pointer()