# 2022/10/30
N = int(input())
data = list(map(int, input().split()))
ans = 0
my = max(data)
# 결국 가장 작은 값에 사서 큰 값을 만드는 식
for value in data:
  # 내 주식보다 값이 싸다면 그걸 사본다.
  if my > value:
    my = value
  # 아니면 팔아보고 값이 크다면 수익 갱신
  else:
    ans = max(ans, value - my)
# 출력
print(ans)
