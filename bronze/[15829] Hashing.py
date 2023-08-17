# 2023/08/12 Implementation, String, Hashing
# https://www.acmicpc.net/problem/15829
L = int(input())
data = input()
res = 0
for i in range(L):
  res += (ord(data[i]) - 96) * (31 ** i)
print(res % 1234567891) # 정답 출력