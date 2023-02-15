# 2023/02/15 Greedy
# https://codeforces.com/contest/1792/problem/A
T = int(input())
for _ in range(T):
  N = int(input())
  arr = sorted(list(map(int,input().split())))
  p = 0
  while arr:
    now = arr.pop(0)
    if now > 0:
      if now == 1 and arr: # 2이상인 경우는 따로 잡는게 이득이다.
        arr[0] -= 1 # 다음 칸 감소
      p += 1
  # 정답 출력
  print(p)