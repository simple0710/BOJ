# 2022/10/30
n = int(input())
data = list(map(int,input().split()))
ans = set()
data.sort()
cnt = 0
# 결국 남는 마트료시카의 수는 가장 많이 있는 크기의 개수이다.
for i in data:
  ans.add(data.count(i))
print(max(ans))