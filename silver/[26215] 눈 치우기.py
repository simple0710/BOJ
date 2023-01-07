# 2022/12/13 그리디
# https://www.acmicpc.net/problem/26215
N = int(input())
arr = list(map(int,input().split()))

res = 0
# 치울 곳이 두 곳 이상인 경우
while len(arr) > 1:
  # 내림차순으로 정렬
  arr.sort(reverse=True)
  # 0이면 청소 목록에서 제거
  if arr[1] == 0:
    del arr[1]
    continue
  # 청소
  arr[0] -= 1
  arr[1] -= 1
  res += 1
# 남은 눈 제거
res += arr[0]

# 정답 출력
if res > 1440:
  print(-1)
else:
  print(res)