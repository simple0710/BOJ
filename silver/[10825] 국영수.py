# 2023/06/09 Sorting
# https://www.acmicpc.net/problem/10825
data = []
for _ in range(int(input())):
  name, a, b, c = map(str,input().split())
  data.append([name, a, b, c])
data.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0])) # 정렬
# 정답 출력
for value in data:
  print(value[0])