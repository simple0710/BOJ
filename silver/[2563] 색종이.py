# 2022/11/20 구현
data = [[0] * 100 for _ in range(100)]

for _ in range(int(input())):
  # 위치 입력
  x, y = map(int,input().split())
  # 해당 위치에 맞게 값을 1로 지정
  for i in range(y, y + 10):
    for j in range(x, x + 10):
      data[i][j] = 1

res = 0
# 전 지역을 탐색해서 나온 1의 개수를 res에 추가
for i in data:
  res += i.count(1)

# 정답 출력
print(res)