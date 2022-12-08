# 2022/12/01 그리디 알고리즘
# https://www.acmicpc.net/problem/1700
N, K = map(int,input().split())
arr = list(map(int,input().split()))

mtap = []
res = 0
# 전 범위 탐색
for i in range(K):
  # 만약 멀티탭에 없는 경우
  if arr[i] not in mtap:
    if len(mtap) == N:
      res += 1
      check = 0
      for x in mtap:
        # 앞으로 쓸 일 없으면 제거할 값으로 지정한다.
        if x not in arr[i:]:
          r_key = x
          break
        else:
          c = arr[i:].index(x)
          # 가장 멀리있는 값을 멀티탭에서 제거할 값으로 지정한다.
          if c > check:
            check = c
            r_key = x
      mtap.remove(r_key)
    mtap.append(arr[i])

# 정답 출력
print(res)

