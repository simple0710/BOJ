# 나무의 수와 필요한 나무 수를 입력 받는다.
n, m = map(int,input().split())
data = list(map(int,input().split()))

start = 0
end = max(data)

while (start <= end):
  total = 0 # 자른 나무의 총합
  mid = (start + end) // 2
  # 나무를 자를 수 있다면 잘라서 total에 추가한다.
  for x in data:
    if x >= mid:
      total += x - mid
  # 만약 부족하다면 너무 크게 자른 것이므로 end = mid - 1
  if total < m:
    end = mid - 1
  # 같거나 더 많다면 적당히 자른 것이므로 start = mid + 1
  else:
    start = mid + 1

print(end)