# 2023/04/05 Sorting, TwoPointer
# https://www.acmicpc.net/problem/7795
for _ in range(int(input())):
  N, M = map(int,input().split())
  A = sorted(list(map(int,input().split())), reverse = True)
  B = sorted(list(map(int,input().split())))
  res = 0
  e = M - 1
  # 탐색 시작
  for i in A:
    while e >= 0:
      if B[e] < i: # 해당 값보다 큰 경우
        # e + 1 만큼의 쌍이 생성된다.
        res += e + 1
        break
      else:
        e -= 1
  # 정답 출력
  print(res)