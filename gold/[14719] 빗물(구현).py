# 입력을 받는다.
n, m = map(int, input().split())
data = list(map(int,input().split()))

total = 0
# 좌, 우의 벽이 자신보다 낮다면 물이 고이지 않는다.
for i in range(1, m - 1):
  # 좌, 우의 벽을 구한다.
  left_max = max(data[:i])
  right_max = max(data[i+1:])

  # 가장 작은 벽의 크기
  compare = min(left_max, right_max)
  # 자신보다 큰 벽이 있다면 "큰 벽 - 자신" 만큼의 물이 고인다.
  if data[i] < compare:
    total += compare - data[i]

print(total)