# 이분 탐색
k, n = map(int, input().split())
data = list()
result = 0

for _ in range(k):
  data.append(int(input()))

start = 1
end = max(data)

result = 0
while (start <= end):
  total = 0
  # 중간 값을 구한다
  mid = (start + end) // 2
  # 데이터를 확인해서 자를려는 값보다 크다면 자르고 total에 추가
  for x in data:
    if x > mid:
      total += x // mid
  # total이 n보다 작다면 mid - 1
  ## mid가 크기 때문에 많은 전선을 자르지 못한 것
  if total < n:
    end = mid - 1
  # total이 n보다 크거나 작은 경우 결과값 저장
  else:
    result = mid
    start = mid + 1

print(result)