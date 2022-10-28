n = int(input())
ans = 0
# (n // i) * i
for i in range(1, n + 1):
  ans += (n // i) * i
print(ans)